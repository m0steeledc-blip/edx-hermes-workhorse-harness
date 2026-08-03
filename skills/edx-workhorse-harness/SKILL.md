---
name: edx-workhorse-harness
description: Master autonomous execution framework using the EDX Hermes Workhorse + Advisor Harness. Dispatches tasks to fast workhorse models, catches tool errors, auto-escalates to High-Reasoning Advisors, mines ChatML datasets, updates Claude digests, and syncs to GitHub automatically.
---

# EDX Workhorse + Advisor Autonomous Execution Harness

## Purpose
Enables 100% hands-free, autonomous execution for ANY complex coding, refactoring, feature implementation, or data mining task across the entire `antigravity-workspace`.

## Core Capabilities & Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                 HIGH-REASONING ADVISORS                     │
│  • Antigravity (Gemini 3.6 Flash) ──► Architecture & Code   │
│  • Nous Portal Free Tier          ──► Multi-Tool Planning    │
└──────────────┬──────────────────────────────┬───────────────┘
               │ (Directives & Blueprints)    │ (Escalations on failure)
               ▼                              │
┌─────────────────────────────────────────────┴───────────────┐
│                LOCAL / FAST WORKHORSE                       │
│  • Groq llama-3.3-70b / Ollama Qwen 2.5                    │
│  • High-speed, low-cost tool execution & code generation    │
└─────────────────────────────────────────────────────────────┘
```

## Autonomous Workflow Execution

When activated on ANY task or project:

1. **Task Dispatch & Execution (`workhorse_harness.py`)**:
   - Dispatches coding or analysis prompts to the fast workhorse model.
   - Monitors tool calls and execution tracebacks.
   - **Auto-Escalation**: On tool failure or reasoning loops, automatically escalates the full context + error traceback to the High-Reasoning Advisor tier (`pro` subagent).

2. **Autonomous Trajectory Mining (`mine_trajectories.py`)**:
   - Extracts all successful multi-turn tool-use cycles into ChatML JSONL format (`dataset.jsonl`).
   - Filters out failed turns to build a high-precision training dataset.

3. **Claude Digest Auto-Update (`generate_claude_digest.py`)**:
   - Compiles new discoveries, code structures, and architecture updates into `docs/EO_Discovered_Invariants_For_Claude.md` (or general project digest) for seamless Claude Desktop collaboration.

4. **Background EOD Sync & GitHub Push (`eod_trajectory_sync.py`)**:
   - Automatically commits updated code, scripts, and digests to GitHub.
   - Packages dataset for 5:00 PM `HPUSH` mesh transport to VPS (`~/VPS_DROP/`).

## How to Invoke Autonomously
Simply activate this skill whenever starting ANY project task, refactor, or automation run:
- Auto-delegates heavy reasoning to `pro` subagents.
- Auto-recovers from execution errors without user intervention.
- Auto-saves checkpoints before modifying any file.
