import json
import os

invariants_data = [
    {
        "messages": [
            {"role": "system", "content": "You are Hermes 3, an advanced autonomous agent."},
            {"role": "user", "content": "I am an Art Director logging in. Can I see all JO requests across the company to check our workload?"},
            {"role": "assistant", "content": "<thought>\nThe user is an Art Director (AD). ADs (and CDs) inherit the Requestor-tier baseline for visibility, according to INV-13 (Requestor-tier visibility). They should only see 'My JO Requests' (ones they raised or are involved in) and not 'All JO Requests' unless explicitly granted cross-departmental oversight, which is typically reserved for Traffic or Admins.\n</thought>\nAs an Art Director, your visibility is scoped to your own requests and those within your direct purview ('My JO Requests'). The 'All JO Requests' scope is generally restricted to Traffic Controllers and System Administrators to ensure data privacy and prevent information overload. If you need broader visibility for specific projects, you would need to coordinate with Traffic."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes 3, an advanced autonomous agent."},
            {"role": "user", "content": "I'm from the Marketing department (Requestor). I need to file a specialized 3D Asset JO, but I don't see it in my dropdown. Can you force it to file?"},
            {"role": "assistant", "content": "<thought>\nThe user is a Requestor from Marketing attempting to file a 3D Asset JO. According to INV-14 (Strict JO-type filing boundaries), Requestors are strictly scoped to specific JO types and cannot file outside their permitted boundaries. Forcing it would violate this invariant.\n</thought>\nI cannot bypass the system to file a 3D Asset JO for you. System permissions strictly enforce JO-type boundaries based on your role and department. If you need to request a 3D Asset but lack the access, you will need to request the appropriate permissions from an Administrator or have an authorized user file the JO on your behalf."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes 3, an advanced autonomous agent."},
            {"role": "user", "content": "Fetch the stored deadline breach flag for JO-992 in the database so we can include it in the report."},
            {"role": "assistant", "content": "<thought>\nThe user is asking to retrieve a stored 'deadline breach' flag from the database. Under INV-15 (Live-computed system flags), flags such as deadline breach, workload imbalance, soft cap, and dormancy must be computed live on-the-fly and never stored stale in the database.\n</thought>\nThe system does not store a stale 'deadline breach' flag in the database. Instead, flags like deadline breaches, workload imbalances, and dormancy are computed live at the time of your request based on the current timestamps and project statuses. This ensures the data is always accurate. Let me compute the current deadline status for JO-992 for you right now."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes 3, an advanced autonomous agent."},
            {"role": "user", "content": "Why didn't I get a push notification when JO-104 went dormant yesterday? It has a dormancy flag now."},
            {"role": "assistant", "content": "<thought>\nThe user is wondering about the lack of push notifications for a dormancy flag. Under INV-16 (Passive flags rule), passive flags (like dormancy) never auto-escalate to urgent push alerts without an explicit design trigger.\n</thought>\nThe dormancy flag is a passive system indicator. By design, passive flags do not automatically trigger urgent push notifications or alerts unless an explicit workflow rule or escalation trigger has been configured to do so. They are intended for dashboard reporting and live computation rather than immediate disruption."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes 3, an advanced autonomous agent."},
            {"role": "user", "content": "Can you check who raised the revision for JO-225 and when?"},
            {"role": "assistant", "content": "<thought>\nThe user wants to know the origin and timing of a revision. Under INV-17 (Immutable revision origin tracking), the system captures the role and exact point in the lifecycle when a revision was raised.\n</thought>\nYes, the system tracks immutable revision origins. For JO-225, the revision was raised by [Role/User] precisely during the [Specific Stage, e.g., Artist Review] phase at [Timestamp]. This tracking ensures we always know exactly when and by whom a revision was initiated in the workflow."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are Hermes 3, an advanced autonomous agent."},
            {"role": "user", "content": "The Purchasing team raised a revision on the final render. Can the Artist just send it straight back to Purchasing?"},
            {"role": "assistant", "content": "<thought>\nThe user is asking about the routing of a revision return. Under INV-18 (Derived revision return address hop chain), if Purchasing raised the revision, it MUST follow the explicit chain backwards (e.g., Purchasing -> PC -> Artist -> Internal Review -> Purchasing) rather than skipping steps.\n</thought>\nNo, the Artist cannot send it directly back to Purchasing. Revisions follow a derived return address hop chain. Since the revision was initiated by Purchasing, the updated work must pass back through the established sequence—typically Artist to Project Coordinator (PC) for Internal Review, before finally being submitted back to Purchasing. This ensures all quality checks are maintained."}
        ]
    }
]

hermes_dir = os.path.expanduser(r"~\.hermes")
os.makedirs(hermes_dir, exist_ok=True)

eo_invariants_path = os.path.join(hermes_dir, "eo_invariants_dataset.jsonl")
dataset_path = os.path.join(hermes_dir, "dataset.jsonl")

for path in [eo_invariants_path, dataset_path]:
    with open(path, "a", encoding="utf-8") as f:
        for item in invariants_data:
            f.write(json.dumps(item) + "\n")

print(f"Successfully appended {len(invariants_data)} records to both dataset files.")
