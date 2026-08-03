import json
import re
from pathlib import Path

def parse_verbatim_invariants(v8_path):
    text = v8_path.read_text(encoding='utf-8')
    # Regex to extract each INV line: e.g. - **INV-01**: ...
    pattern = re.compile(r'- \*\*INV-(\d+)\*\*:\s*(.+?)(?=\n- \*\*INV-\d+\*\*:|\n\n## |\Z)', re.DOTALL)
    matches = pattern.findall(text)
    
    trajectories = []
    for inv_num, inv_text in matches:
        clean_text = inv_text.strip().replace('\n', ' ')
        clean_text = re.sub(r'\s+', ' ', clean_text)
        
        trajectories.append({
            "messages": [
                {"role": "system", "content": "You are the EO Creative Ops Compliance Engine. You provide verbatim rules from EO_System_Invariants_v8.md."},
                {"role": "user", "content": f"What is the exact requirement of INV-{inv_num}?"},
                {"role": "assistant", "content": f"Per INV-{inv_num}: {clean_text}"}
            ]
        })
    return trajectories

def generate_verbatim_dataset(output_path):
    docs_dir = Path(r"C:\Users\ecayabyab\antigravity-workspace\eo-creatives-ops\official docs")
    v8_path = docs_dir / "EO_System_Invariants_v8.md"
    
    if not v8_path.exists():
        raise FileNotFoundError(f"Missing {v8_path}")
        
    trajectories = parse_verbatim_invariants(v8_path)
    
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        for t in trajectories:
            f.write(json.dumps(t) + "\n")
            
    print(f"Successfully generated {len(trajectories)} 100% verbatim invariant entries at {output_path}")

if __name__ == "__main__":
    out_file = r"C:\Users\ecayabyab\.hermes\eo_invariants_dataset.jsonl"
    generate_verbatim_dataset(out_file)
