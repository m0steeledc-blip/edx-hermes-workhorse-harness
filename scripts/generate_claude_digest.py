import os
from pathlib import Path
from datetime import datetime

def generate_claude_digest():
    print("Generating 100% Pure Verbatim Invariants Digest for Claude Desktop...")
    
    # Authoritative doc paths
    inv_v8_path = Path(r"C:\Users\ecayabyab\antigravity-workspace\eo-creatives-ops\official docs\EO_System_Invariants_v8.md")
    
    output_dir = Path(r"C:\Users\ecayabyab\antigravity-workspace\edx-hermes-workhorse-harness\docs")
    output_dir.mkdir(parents=True, exist_ok=True)
    digest_path = output_dir / "EO_Discovered_Invariants_For_Claude.md"
    
    if not inv_v8_path.exists():
        raise FileNotFoundError(f"Authoritative spec not found at {inv_v8_path}")
        
    v8_content = inv_v8_path.read_text(encoding='utf-8')
    
    # Pure verbatim output - zero extra summary blocks, zero commentary decoration
    digest_path.write_text(v8_content, encoding='utf-8')
    print(f"Successfully wrote 100% pure verbatim digest to {digest_path}")

if __name__ == "__main__":
    generate_claude_digest()
