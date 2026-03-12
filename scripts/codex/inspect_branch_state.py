#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


def run_command(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)


def run_git(repo: Path, *args: str) -> str:
    result = run_command(["git", *args], repo)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git command failed: {' '.join(args)}")
    return result.stdout.strip()


def try_git(repo: Path, *args: str) -> tuple[bool, str]:
    result = run_command(["git", *args], repo)
    return result.returncode == 0, (result.stdout or result.stderr).strip()


def parse_remote_repo(remote_url: str) -> str | None:
    if remote_url.startswith("https://github.com/"):
        repo = remote_url.removeprefix("https://github.com/")
    else:
        match = re.match(r"git@github\.com:(.+)", remote_url)
        if not match:
            return None
        repo = match.group(1)
    if repo.endswith(".git"):
        repo = repo[:-4]
    parts = repo.split("/")
    if len(parts) != 2:
        return None
    return repo


def rev_counts(repo: Path, left: str, right: str) -> tuple[int, int] | None:
    ok, output = try_git(repo, "rev-list", "--left-right", "--count", f"{left}...{right}")
    if not ok or not output:
        return None
    left_count, right_count = output.split()
    return int(left_count), int(right_count)


def detect_pr(repo: Path, branch: str) -> dict[str, object]:
    if shutil.which("gh") is None:
        return {"status": "unavailable", "reason": "gh not found"}

    ok, remote_url = try_git(repo, "remote", "get-url", "origin")
    if not ok:
        return {"status": "unavailable", "reason": "origin remote not found"}

    remote_repo = parse_remote_repo(remote_url)
    if not remote_repo:
        return {"status": "unavailable", "reason": "origin remote is not a supported GitHub URL"}

    result = run_command(
        ["gh", "pr", "list", "--repo", remote_repo, "--head", branch, "--json", "number,title,url,state,isDraft"],
        repo,
    )
    if result.returncode != 0:
        return {"status": "unavailable", "reason": (result.stderr or result.stdout).strip()}

    payload = json.loads(result.stdout or "[]")
    if not payload:
        return {"status": "missing"}

    pr = payload[0]
    return {
        "status": "existing",
        "number": pr.get("number"),
        "title": pr.get("title"),
        "url": pr.get("url"),
        "state": pr.get("state"),
        "draft": pr.get("isDraft", False),
    }


def choose_next_action(
    clean_worktree: bool,
    conflicts: list[str],
    upstream: str | None,
    base_divergence: tuple[int, int] | None,
    upstream_divergence: tuple[int, int] | None,
    pr_status: dict[str, object],
) -> str:
    if conflicts:
        return "resolve-conflicts"
    if not clean_worktree:
        return "review-local-changes-before-sync"
    if base_divergence and base_divergence[0] > 0:
        return "merge-or-rebase-base"
    if upstream is None:
        return "push-branch"
    if upstream_divergence and upstream_divergence[1] > 0:
        if pr_status.get("status") == "existing":
            return "push-and-update-pr"
        return "push-local-commits"
    if base_divergence and base_divergence[1] > 0:
        if pr_status.get("status") == "missing":
            return "create-pr"
        if pr_status.get("status") == "existing":
            return "pr-open-no-sync-needed"
        return "check-pr-status-with-escalation"
    if pr_status.get("status") == "existing":
        return "pr-open-no-sync-needed"
    return "no-action"


def build_payload(repo: Path, base: str, head: str | None) -> dict[str, object]:
    repo = repo.resolve()
    if not repo.exists() or not repo.is_dir():
        raise RuntimeError(f"repo path is not a directory: {repo}")

    current_branch = head or run_git(repo, "branch", "--show-current")
    if not current_branch:
        raise RuntimeError("could not determine branch name")

    status_lines = run_git(repo, "status", "--porcelain").splitlines()
    clean_worktree = len(status_lines) == 0
    conflicts = [line for line in run_git(repo, "diff", "--name-only", "--diff-filter=U").splitlines() if line]

    upstream_ok, upstream_output = try_git(repo, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
    upstream = upstream_output if upstream_ok and upstream_output else None

    base_divergence = rev_counts(repo, base, current_branch)
    upstream_divergence = rev_counts(repo, upstream, current_branch) if upstream else None
    pr_status = detect_pr(repo, current_branch)

    payload = {
        "repo": str(repo),
        "current_branch": current_branch,
        "base_branch": base,
        "upstream": upstream,
        "clean_worktree": clean_worktree,
        "conflicts": conflicts,
        "base_divergence": {
            "base_ahead": base_divergence[0],
            "head_ahead": base_divergence[1],
        } if base_divergence else None,
        "upstream_divergence": {
            "upstream_ahead": upstream_divergence[0],
            "head_ahead": upstream_divergence[1],
        } if upstream_divergence else None,
        "pr_status": pr_status,
    }
    payload["next_action"] = choose_next_action(
        clean_worktree,
        conflicts,
        upstream,
        base_divergence,
        upstream_divergence,
        pr_status,
    )
    return payload


def print_text(payload: dict[str, object]) -> None:
    print("Branch sync inspection")
    print(f"repo: {payload['repo']}")
    print(f"current_branch: {payload['current_branch']}")
    print(f"base_branch: {payload['base_branch']}")
    print(f"upstream: {payload['upstream'] or '(none)'}")
    print(f"clean_worktree: {payload['clean_worktree']}")
    conflicts = payload["conflicts"]
    if conflicts:
        print("conflicts:")
        for path in conflicts:
            print(f"- {path}")
    else:
        print("conflicts: none")
    print(f"base_divergence: {json.dumps(payload['base_divergence'])}")
    print(f"upstream_divergence: {json.dumps(payload['upstream_divergence'])}")
    print(f"pr_status: {json.dumps(payload['pr_status'])}")
    print(f"next_action: {payload['next_action']}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect branch sync and PR state without mutating the repo.")
    parser.add_argument("--repo", required=True, help="Repository path to inspect.")
    parser.add_argument("--base", required=True, help="Base branch name, usually main.")
    parser.add_argument("--head", default="", help="Optional head branch override. Defaults to current branch.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    args = parser.parse_args()

    payload = build_payload(Path(args.repo), args.base, args.head or None)
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print_text(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
