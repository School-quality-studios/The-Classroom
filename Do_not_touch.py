import json
import os

# --- I. THE GHOST DATABASE TEMPLATE ---
# This dictionary represents your 5-student ledger.
MASTER_LEDGER = {
    "studio_metadata": {
        "org": "School Quality Studios",
        "capacity": 5
    },
    "class_ledger": [
        {"id": "turtleboyagain120", "score": 100, "status": "ARCHITECT"},
        {"id": "Student_Node_02", "score": 0, "status": "INITIALIZING"},
        {"id": "Student_Node_03", "score": 0, "status": "INITIALIZING"},
        {"id": "Student_Node_04", "score": 0, "status": "INITIALIZING"},
        {"id": "Student_Node_05", "score": 0, "status": "INITIALIZING"}
    ]
}

def run_score_sync():
    # Detect who is pushing code right now
    student_id = os.getenv('GITHUB_ACTOR', 'Guest_Node')
    ledger_file = 'DATABASE.json'

    # Initialize the file if it doesn't exist
    if not os.path.exists(ledger_file):
        print(f"⚠️ [SYSTEM] Initializing Master Ledger...")
        data = MASTER_LEDGER
    else:
        with open(ledger_file, 'r') as f:
            data = json.load(f)

    # --- II. SCORE ADDING LOGIC ---
    student_found = False
    for entry in data['class_ledger']:
        if entry['id'] == student_id:
            # Add +20 points per successful sync
            entry['score'] += 20
            if entry['score'] >= 100:
                entry['status'] = 'MASTERED'
                entry['score'] = 100 # Cap at 100
            student_found = True
            break

    # If they aren't on the list and there's room, add them
    if not student_found and len(data['class_ledger']) < 5:
        data['class_ledger'].append({"id": student_id, "score": 20, "status": "INITIALIZING"})

    # --- III. SAVE TO GHOST DATABASE ---
    with open(ledger_file, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"✅ [SUCCESS] {student_id} updated. Syncing to Ghost Database...")

if __name__ == '__main__':
    run_score_sync()
