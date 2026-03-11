# GitHub Branch Protection Checklist

Use this checklist when applying manual GitHub settings that cannot be enforced from the repo alone.

## Branch Protection For `main`

- [ ] Protect the `main` branch.
- [ ] Require pull requests before merging.
- [ ] Require at least one review before merge.
- [ ] Require status checks before merge.
- [ ] Restrict direct pushes to `main` if that matches the team workflow.
- [ ] Require branches to be up to date before merge if status checks are enabled.

## Ownership And Review

- [ ] Keep [`.github/CODEOWNERS`](../../.github/CODEOWNERS) enabled if the team wants automatic review requests.
- [ ] Consider enforcing CODEOWNERS review for changes under `docs/`, `agents/`, `schemas/`, `workflows/`, and `legacy/poc/`.

## Legacy Freeze

- [ ] Treat `legacy/poc/` as frozen archived material.
- [ ] Reject PRs that introduce active new work under `legacy/` unless the change is an explicitly approved legacy task.
- [ ] Use review guidance and branch protection settings to keep `legacy/poc/` read-only by default.

## Notes

- The repo operating model lives in [README.md](../../README.md), [docs/guardrails.md](../guardrails.md), and [agents/coding_agent_contract.md](../../agents/coding_agent_contract.md).
- Manual GitHub settings should reinforce those repo rules rather than replace them.
