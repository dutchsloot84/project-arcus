# Legacy POC: Enterprise Synthetic Data Hub

This directory preserves the original Project Arcus proof of concept in an archived location. It remains available for reference and demo playback, but it is frozen unless a future task explicitly targets `legacy/poc/`.

## Status

- Archived proof of concept
- Not the active development path for Project Arcus
- Frozen unless explicitly requested

## Run From The Archived Location

From the repository root:

```powershell
cd legacy/poc
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .[dev]
```

Unix-style shells:

```bash
cd legacy/poc
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .[dev]
```

## Demo Commands

Run the guided demo flow:

```powershell
cd legacy/poc
python scripts/demo_validate.py
python scripts/run_demo_flow.py
```

Or use the existing bootstrap helpers:

```powershell
cd legacy/poc
./scripts/bootstrap_and_demo.ps1
```

```bash
cd legacy/poc
bash scripts/bootstrap_and_demo.sh
```

## Outputs

- Demo samples live under `legacy/poc/data/demo_samples/`
- Snapshot outputs live under `legacy/poc/data/snapshots/`
- Demo run artifacts land under `legacy/poc/data/demo_runs/`
- Script-managed demo run artifacts also appear under `legacy/poc/scripts/data/demo_runs/`

## Notes

- Existing docs inside this archive were written for the original repo root and may still refer to root-relative paths from the POC era.
- The active repo operating system now lives at the repository root. Start there for current workflows, governance, and agent instructions.