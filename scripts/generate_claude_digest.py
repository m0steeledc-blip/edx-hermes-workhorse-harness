import sys
from pathlib import Path

# Canonical Single Source of Truth
CANONICAL_SPEC_PATH = Path(r"C:\Users\ecayabyab\antigravity-workspace\eo-creatives-ops\official docs\EO_System_Invariants_v8.md")

def verify_canonical_spec():
    if not CANONICAL_SPEC_PATH.exists():
        print(f"ERROR: Canonical spec file missing at {CANONICAL_SPEC_PATH}")
        sys.exit(1)
    
    print(f"✅ Verified Canonical Spec File (Single Source of Truth): {CANONICAL_SPEC_PATH}")
    return CANONICAL_SPEC_PATH.read_text(encoding='utf-8')

if __name__ == "__main__":
    verify_canonical_spec()
