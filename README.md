# EDX Hermes Workhorse + Advisor Harness

A production-grade dual-model agentic AI ecosystem combining ultra-fast local execution with high-reasoning free-tier advisors, automated trajectory mining, and 5:00 PM EOD dataset synchronization.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                 HIGH-LEVEL ADVISORS                         │
│  • Antigravity (Gemini 3.6 Flash) ──► Architecture & Code   │
│  • Hermes Free Tier (laguna-s)   ──► Multi-Tool Planning    │
└──────────────┬──────────────────────────────┬───────────────┘
               │ (Plans & Instructions)       │ (Escalations on errors)
               ▼                              │
┌─────────────────────────────────────────────┴───────────────┐
│                LOCAL WORKHORSE MODEL                        │
│  • Fast Model (Ollama 3B/7B or Groq llama-3.3-70b)           │
│  • High-volume, repetitive, low-latency execution           │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Repository Structure

- `scripts/mine_trajectories.py`: Connects to Hermes SQLite `state.db` and extracts multi-turn trajectories to Hermes 3 ChatML JSONL format.
- `scripts/mine_eo_invariants.py`: Synthesizes ChatML test trajectories covering all 37 EO System Invariants (INV-01 to INV-37).
- `scripts/workhorse_harness.py`: Dispatches tasks to the fast workhorse model; auto-catches failures and escalates context to the High-Level Advisor.
- `scripts/eod_trajectory_sync.py`: 5:00 PM automated harvester script registered in Windows Task Scheduler (`EDX-EOD-Harvester`).
- `datasets/`: Contains harvested JSONL datasets (`dataset.jsonl`, `eo_invariants_dataset.jsonl`) for local fine-tuning via Axolotl.
- `docs/`: Comprehensive technical specs, 37 Invariants reference, and findings/results log.

---

## ⚡ Quick Start

### 1. Mine Session Trajectories
```bash
python scripts/mine_trajectories.py --limit 100 --output-file datasets/dataset.jsonl
```

### 2. Mine EO Invariants Dataset
```bash
python scripts/mine_eo_invariants.py --output-file datasets/eo_invariants_dataset.jsonl
```

### 3. Run EOD Harvest & Sync
```bash
python scripts/eod_trajectory_sync.py --force
```

---

## 🔄 Cross-Machine Sync Protocol (OFC ↔ VPS ↔ RIG)

1. **Office Laptop (OFC)**: Mines daily work trajectories every workday at 5:00 PM via `EDX-EOD-Harvester`.
2. **Mesh Transport**: Pushed via `HPUSH` (`local_to_vps_append_sync.py`) to VPS (`~/VPS_DROP/`).
3. **Home PC (RIG)**: Pulls dataset from VPS; fine-tunes local Qwen 2.5 7B / Llama 3.1 8B model via Axolotl GPU training.
