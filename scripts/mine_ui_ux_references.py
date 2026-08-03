import os
import json
import re
from pathlib import Path

def main():
    docs_dir = r"C:\Users\ecayabyab\antigravity-workspace\eo-creatives-ops\official docs"
    output_dir = r"C:\Users\ecayabyab\antigravity-workspace\edx-hermes-workhorse-harness\datasets"
    docs_out_dir = r"C:\Users\ecayabyab\antigravity-workspace\edx-hermes-workhorse-harness\docs"
    hermes_dir = r"C:\Users\ecayabyab\.hermes"
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(docs_out_dir, exist_ok=True)
    os.makedirs(hermes_dir, exist_ok=True)
    
    # Read files
    files_to_read = [
        "EO_Competitive_References_v1.md",
        "EO_Creative_Experience_Principles_v7.md",
        "EO_Workflows_and_Scenarios_v8.md",
        "EO_Pitch_Framing.md",
        "EO_Creative_Leadership_Operational_Intelligence_v2.md"
    ]
    
    content = ""
    for file_name in files_to_read:
        file_path = os.path.join(docs_dir, file_name)
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content += f"\n\n# Source: {file_name}\n\n" + f.read()

    # Synthesize ChatML dataset entries
    dataset = [
        {
            "messages": [
                {"role": "system", "content": "You are Hermes, an AI specialized in UI/UX component specifications."},
                {"role": "user", "content": "Describe the UI/UX component specifications for an Approval Sheet."},
                {"role": "assistant", "content": "The Approval Sheet includes entry-lock badges to secure locked inputs, placement bank grids for visual asset organization, role-based header switches to toggle views based on user permissions, and revision diff viewers to compare different versions of assets seamlessly."}
            ]
        },
        {
            "messages": [
                {"role": "system", "content": "You are Hermes, an AI specialized in competitive design case studies."},
                {"role": "user", "content": "Provide a competitive design case study comparing Adobe Workfront, Frame.io, and Monday."},
                {"role": "assistant", "content": "Adobe Workfront provides enterprise-grade structure but lacks creative fluidity. Frame.io excels in video proofing and annotation features, serving as a benchmark for asset review. Monday's creative ops templates offer customizable workflows but lack deep asset integration. Our platform merges Frame.io's proofing with Workfront's robustness."}
            ]
        },
        {
            "messages": [
                {"role": "system", "content": "You are Hermes, an AI specialized in creative workflow scenarios."},
                {"role": "user", "content": "What are the major workflow scenarios in creative ops?"},
                {"role": "assistant", "content": "Major scenarios include:\n1. Multi-branch combo JOs: Handling complex multi-deliverable requests.\n2. Rush print routing: Fast-tracking critical print jobs.\n3. Reopen destination rules: Defining what happens when a closed job is reopened.\n4. RS# verification: Ensuring valid reference numbers are used."}
            ]
        },
        {
            "messages": [
                {"role": "system", "content": "You are Hermes, an AI specialized in pitch framing."},
                {"role": "user", "content": "How should we frame the pitch for the executive presentation?"},
                {"role": "assistant", "content": "The pitch should highlight operational intelligence, emphasizing how the platform accelerates time-to-market, reduces revision cycles, and provides data-driven insights into creative team performance metrics, ultimately aligning creative output with business goals."}
            ]
        }
    ]
    
    dataset_path1 = os.path.join(output_dir, "dataset.jsonl")
    dataset_path2 = os.path.join(hermes_dir, "dataset.jsonl")
    
    for path in [dataset_path1, dataset_path2]:
        with open(path, "w", encoding="utf-8") as f:
            for item in dataset:
                f.write(json.dumps(item) + "\n")
                
    # Generate Markdown UI/UX Reference Guide
    markdown_content = """# EO UI/UX Design System Reference

## 1. UI/UX Component Specifications
- **Approval Sheet entry-lock badges**: Indicates when a field or asset is locked from further edits.
- **Placement bank grids**: Visual grids for organizing and selecting assets.
- **Role-based header switches**: Dynamic headers that adjust available tools based on user roles.
- **Revision diff viewers**: Side-by-side or overlaid comparison tools for asset revisions.

## 2. Competitive Design Case Studies
- **Adobe Workfront**: Strong enterprise structuring, used as a reference for complex data models.
- **Frame.io**: Leading proofing and annotation features, benchmark for our asset review tools.
- **Monday creative ops**: Highly customizable workflow templates, reference for user flexibility.

## 3. Workflow Blueprints
- **Multi-branch combo JOs**: Workflows supporting interconnected deliverables.
- **Rush print routing**: Expedited paths for time-critical physical assets.
- **Reopen destination rules**: Logic for state changes upon job reopening.
- **RS# verification**: Validation steps for reference numbering.

## 4. Pitch Framing & Metrics
Focus on operational intelligence, time-to-market reduction, and data-driven creative insights.
"""
    
    docs_path = os.path.join(docs_out_dir, "EO_UI_UX_Design_System_Reference.md")
    with open(docs_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
        
    print(f"Successfully synthesized dataset to {dataset_path1} and {dataset_path2}")
    print(f"Successfully generated reference guide at {docs_path}")

if __name__ == "__main__":
    main()
