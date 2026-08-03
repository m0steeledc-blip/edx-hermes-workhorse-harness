import os
import json
from pathlib import Path
from datetime import datetime

def load_jsonl(filepath):
    data = []
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    try:
                        data.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
    return data

def generate_digest():
    workspace_dir = Path(r"C:\Users\ecayabyab\antigravity-workspace\edx-hermes-workhorse-harness")
    datasets_dir = workspace_dir / "datasets"
    docs_dir = workspace_dir / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = docs_dir / "EO_Discovered_Invariants_For_Claude.md"
    
    dataset_file = datasets_dir / "dataset.jsonl"
    invariants_file = datasets_dir / "eo_invariants_dataset.jsonl"
    hermes_file = Path.home() / ".hermes" / "dataset.jsonl"
    
    datasets = {
        "dataset.jsonl": load_jsonl(dataset_file),
        "eo_invariants_dataset.jsonl": load_jsonl(invariants_file),
        "hermes_dataset.jsonl": load_jsonl(hermes_file)
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# EO Creative Ops - Discovered Invariants Digest\n\n")
        f.write(f"**Generated At:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("> **Notice for Claude:** This digest contains the latest harvested trajectories, invariant validations, edge cases, and web app recommendations for the EO Creative Ops platform. Please absorb this context fully to stay up-to-date.\n\n")
        
        for name, data in datasets.items():
            if not data:
                f.write(f"## Digest from `{name}`\n\n")
                f.write(f"*No records found or file does not exist.*\n\n---\n\n")
                continue
            
            f.write(f"## Digest from `{name}`\n\n")
            f.write(f"*Total Records:* {len(data)}\n\n")
            
            for i, record in enumerate(data):
                f.write(f"### Record {i+1}\n")
                if isinstance(record, dict):
                    for k, v in record.items():
                        if isinstance(v, (dict, list)):
                            f.write(f"**{k}:**\n```json\n{json.dumps(v, indent=2)}\n```\n")
                        else:
                            f.write(f"**{k}:** {v}\n")
                else:
                    f.write(f"```json\n{json.dumps(record, indent=2)}\n```\n")
                f.write("\n---\n\n")

if __name__ == "__main__":
    generate_digest()
    print(f"Digest generated successfully at docs/EO_Discovered_Invariants_For_Claude.md")
