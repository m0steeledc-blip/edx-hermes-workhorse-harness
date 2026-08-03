import json
import os

invariants_data = [
    {
        "messages": [
            {"role": "system", "content": "You are Hermes, an expert enterprise system AI."},
            {"role": "user", "content": "How do we store placement records in the new system? (INV-29)"},
            {"role": "assistant", "content": "We use a flat placement record schema. The hierarchy is Mall -> Branch -> Placement flat records. A single record contains the description, WxH, unit, orientation, quantity, and location. We do not use deeply nested sub-records for these attributes."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes, an expert enterprise system AI."},
            {"role": "user", "content": "What are the official filing categories for JOs? (INV-30)"},
            {"role": "assistant", "content": "There are exactly 10 official filing categories: Collaterals, Ecomm, Digital Placement, SGU, Store Opening, Board Up, Signage, POP, Voucher, and Special Project."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes, an expert enterprise system AI."},
            {"role": "user", "content": "How do we check dimensions for proxies? (INV-31)"},
            {"role": "assistant", "content": "The Compile & Label tool performs JO-declared-dimension proxy checking. It verifies that the dimensions declared in the JO match the dimensions of the provided proxy files."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes, an expert enterprise system AI."},
            {"role": "user", "content": "How do we handle proxy vs final file types? (INV-32)"},
            {"role": "assistant", "content": "The system maintains a strict proxy vs final file-type split. Proxies are typically low-resolution JPEGs or PDFs for preview and approval, while final files are high-resolution formats like TIFF, AI, or PSD meant for actual production."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes, an expert enterprise system AI."},
            {"role": "user", "content": "How are approval sheets handled if not all placements are approved at once? (INV-33)"},
            {"role": "assistant", "content": "The system supports partial or staggered approval sheets. Placements can have independent releases, and the system automatically compiles a final sheet encompassing all approved placements once the entire JO is completed."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes, an expert enterprise system AI."},
            {"role": "user", "content": "Can we revise a placement anytime? (INV-34)"},
            {"role": "assistant", "content": "No, placement-level revisions are governed by JO-state-dependent rules. Revisions can only be made during specific states (e.g., 'Draft', 'Pending Revision'), and may be locked or require elevated approvals during states like 'In Production'."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes, an expert enterprise system AI."},
            {"role": "user", "content": "Do we need to show the status of each placement? (INV-35)"},
            {"role": "assistant", "content": "Yes, mandatory per-placement status display is required. Each individual placement within a JO must clearly show its current status (e.g., Approved, Pending, Rejected) in the UI."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes, an expert enterprise system AI."},
            {"role": "user", "content": "Where should I add remarks for a specific item in the JO? (INV-36)"},
            {"role": "assistant", "content": "Remarks must be added at the placement level. Placement-level remarks belong to individual placements, never at the overall JO-level, to ensure clarity on which specific item the comment applies to."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes, an expert enterprise system AI."},
            {"role": "user", "content": "Can I edit placement details after PC Assignment? (INV-37)"},
            {"role": "assistant", "content": "No, placement data is immutable after PC Assignment. All subsequent changes must occur via logged revision workflows. Raw edits are never allowed once assigned to a Production Coordinator."}
        ]
    }
]

file_paths = [
    r"C:\Users\ecayabyab\.hermes\eo_invariants_dataset.jsonl",
    r"C:\Users\ecayabyab\.hermes\dataset.jsonl"
]

for file_path in file_paths:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "a", encoding="utf-8") as f:
        for entry in invariants_data:
            f.write(json.dumps(entry) + "\n")
    print(f"Appended entries to {file_path}")
