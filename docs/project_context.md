# Project Context

## Mission

Project Arcus is evolving from a single proof-of-concept codebase into a reusable operating model for repository-based delivery with human and AI collaborators. The root of this repository is now the canonical place for project intent, operating rules, contracts, and structured context.

## What The Repo Must Optimize For

- Deterministic change planning and reviewability
- Clear separation between active guidance and archived implementation history
- Contract-first collaboration between people and coding agents
- Traceable decisions, manifests, and workflows

## Current State

- The legacy Enterprise Synthetic Data Hub POC has been preserved under `legacy/poc/`.
- Active root-level work is now documentation, governance, workflow, schema, and adapter scaffolding.
- New implementation work should align to the contracts and structure at the repo root before code is added.

## Near-Term Focus

- Stand up the repo operating system artifacts at the root
- Define the initial agent contract and agent registry
- Establish manifest and workflow conventions
- Add adapters, examples, tests, and context assets as active work begins

## Operating Principle

If root guidance and implementation drift, root guidance wins until an ADR or contract update changes it.
