---
name: autonomous-invariant-simulator
description: Autonomous auto-chaining simulation engine that mines, generates, and syncs EO System Invariants (INV-01 to INV-37) and ChatML training trajectories without manual user intervention.
---

# Autonomous Invariant Simulator & Trajectory Engine

## Purpose
Enables 100% autonomous, zero-manual-input background execution for synthesizing EO System Invariants (INV-01 to INV-37), harvesting trajectory datasets, updating the Claude Desktop digest, and committing results to GitHub.

## When to Activate
Activate this skill automatically whenever:
1. The user asks to run invariant simulations, dataset generation, or trajectory harvesting.
2. An autonomous background goal (`/goal`) or EOD task requires trajectory synthesis.
3. The user wants to auto-chain batches of Invariant simulations without manual prompt triggers.

## Architecture & Workflows

### 1. Trajectory Harvesters
- `scripts/mine_trajectories.py`: Connects to `state.db` and extracts multi-turn ChatML trajectories (`dataset.jsonl`).
- `scripts/mine_eo_invariants.py`: Synthesizes ChatML test trajectories covering all 37 EO System Invariants.

### 2. Auto-Chaining Simulation Pipeline
- **Auto-Chaining Protocol**: Launch high-reasoning (`pro`) subagents in sequence to simulate batches of 6 Invariants at a time until 100% coverage (INV-01 to INV-37) is reached.
- **Claude Digest Generation**: Automatically invokes `generate_claude_digest.py` to rebuild `docs/EO_Discovered_Invariants_For_Claude.md`.

### 3. Automated End-of-Day Sync (5:00 PM)
- **Windows Task Scheduler**: `EDX-EOD-Harvester` executes `scripts/eod_trajectory_sync.py --force` daily at 17:00 PHST.
- **Mesh Transport**: `HPUSH` (`local_to_vps_append_sync.py`) pushes `dataset.jsonl` to VPS (`~/VPS_DROP/`) for evening training on RIG.

## Operational Instructions

### Execute Full Autonomous Batch Suite
```powershell
python scripts/mine_eo_invariants.py
python scripts/generate_claude_digest.py
python scripts/eod_trajectory_sync.py --force
git commit -am "auto: sync harvested invariant datasets and digest"
git push origin master
```

## Durable Pitfalls & Invariants
- **INV-01 to INV-37**: Never bypass lifecycle state machine, entry-locks, or derived revision return paths.
- **No Manual Crons**: Run via subagent auto-chaining or background Task Scheduler, never force manual user prompt triggers.
