import os
import json
from pathlib import Path

def main():
    docs_dir = Path(r"C:\Users\ecayabyab\antigravity-workspace\eo-creatives-ops\official docs")
    output_dir = Path(r"C:\Users\ecayabyab\antigravity-workspace\edx-hermes-workhorse-harness\datasets")
    docs_out_dir = Path(r"C:\Users\ecayabyab\antigravity-workspace\edx-hermes-workhorse-harness\docs")
    hermes_dir = Path(r"C:\Users\ecayabyab\.hermes")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    docs_out_dir.mkdir(parents=True, exist_ok=True)
    hermes_dir.mkdir(parents=True, exist_ok=True)
    
    files_to_read = [
        ("EO_Competitive_References_v1.md", "Competitive Case Studies & Industry Benchmarks"),
        ("EO_Creative_Experience_Principles_v7.md", "Creative Experience Principles & UI Patterns"),
        ("EO_Pitch_Framing.md", "Executive Pitch Framing & Presentation Narrative"),
        ("EO_Creative_Leadership_Operational_Intelligence_v2.md", "Creative Leadership Operational Intelligence"),
        ("EO_Workflows_and_Scenarios_v8.md", "EO Workflows & End-to-End Scenarios")
    ]
    
    master_reference_text = "# EO Creative Ops — UI/UX Design System & Competitive Reference Library\n\n"
    master_reference_text += "> **Verbatim Reference Compilation** from official platform design documents.\n\n"
    
    for file_name, title in files_to_read:
        file_path = docs_dir / file_name
        if file_path.exists():
            content = file_path.read_text(encoding='utf-8')
            master_reference_text += f"---\n\n## 📚 {title} (`{file_name}`)\n\n"
            master_reference_text += content + "\n\n"
            
    # Write master reference guide
    ref_guide_path = docs_out_dir / "EO_UI_UX_Design_System_Reference.md"
    ref_guide_path.write_text(master_reference_text, encoding='utf-8')
    print(f"Successfully generated 100% verbatim UI/UX Reference Guide at {ref_guide_path}")

    # Read invariants dataset and combine into dataset.jsonl
    eo_inv_file = hermes_dir / "eo_invariants_dataset.jsonl"
    dataset_out = output_dir / "dataset.jsonl"
    hermes_dataset_out = hermes_dir / "dataset.jsonl"
    
    trajectories = []
    if eo_inv_file.exists():
        with open(eo_inv_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    trajectories.append(line.strip())
                    
    # Add UI/UX Verbatim Q&A entries
    ui_ux_entries = [
        {"role": "system", "content": "You are the EO UI/UX Design System Expert."},
        {"role": "user", "content": "What are the core competitive benchmarks for the EO Creative Ops platform?"},
        {"role": "assistant", "content": "Per EO_Competitive_References_v1.md: The platform merges Frame.io's proofing and annotation fluidity with Adobe Workfront's enterprise data structure and Monday's role-based flexibility, eliminating spreadsheet friction."}
    ]
    trajectories.append(json.dumps({"messages": ui_ux_entries}))

    for path in [dataset_out, hermes_dataset_out]:
        with open(path, "w", encoding="utf-8") as f:
            for t in trajectories:
                f.write(t + "\n")
                
    print(f"Successfully updated master dataset with {len(trajectories)} entries at {dataset_out}")

if __name__ == "__main__":
    main()
