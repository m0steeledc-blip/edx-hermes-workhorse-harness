# Findings and Results Log

## Summary of Empirical Results (August 3, 2026)

### 1. Hermes Agent v0.19.1 Core Toolset Performance Batch
- **Deployment**: Successfully updated across both **Local (OFC)** and **VPS (`edx-vps`)** (`upstream a6defd4f`).
- **Schema Diet**: -40% tool definition overhead (~700 tokens saved per request).
- **Skill Deduplication**: ~24.8K tokens saved per repeat skill view.
- **File Read Optimization**: 2,000-line read limit (44% of truncated reads become single-call).
- **Execution Gains**: -21% LLM turns, -29% tool calls, ~23% faster wall clock completion, zero tool errors.

---

### 2. EO Creative Ops 37 System Invariants Synthesis
- **Source Documents**: `EO_Creative_Ops_Platform_Spec_v4.md` & `EO_System_Invariants_v8.md`.
- **Harvested Trajectories**: Initial 6 structured ChatML test trajectories synthesized covering:
  - **INV-01**: Derived row-level lifecycle stages (Submitted ➔ PC Assignment ➔ In Layout ➔ Internal Review ➔ Revision ➔ Pending Release ➔ Printing/Purchasing ➔ Closed).
  - **INV-02**: CD sign-off mandatory inside Internal Review.
  - **INV-18**: Derived revision routing (`Purchasing ➔ PC ➔ Artist ➔ Internal Review ➔ Purchasing`).
  - **INV-19 / INV-20 / INV-27**: In-house vs purchasing print routing & RS# validation rules.
  - **INV-23**: Entry-lock concurrency.
  - **INV-29 / INV-30**: Flat placement schema across 10 official JO categories.

---

### 3. Automated 5:00 PM EOD Harvester Execution
- **Task Scheduler Registration**: `EDX-EOD-Harvester` (Status: `Ready`).
- **Trigger Window**: Daily at 5:00 PM (17:00 PHST).
- **Aggregated Output**: `datasets/dataset.jsonl` (compiled from session trajectories + invariant datasets).
