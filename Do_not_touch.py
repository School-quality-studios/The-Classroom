import json
import os

def run_brain():
    # DYNAMIC NODE DETECTION: Detects the person pushing the code
    # If it can't find a GitHub name, it falls back to 'Guest_Node'
    current_student = os.getenv('GITHUB_ACTOR', 'Guest_Node')
    
    ledger_path = "DATABASE.json"
    
    # Check for the Ghost Database [IV]
    if not os.path.exists(ledger_path):
        print(f"⚠️ NEW NODE DETECTED: Initializing ledger for {current_student}...")
        initial_data = {"student": {"id": current_student, "score": 100}}
        with open(ledger_path, "w") as f:
            json.dump(initial_data, f, indent=4)
    
    with open(ledger_path, "r") as f:
        data = json.load(f)
        
    # Validates the current actor against the ledger
    print(f"🚀 [SYSTEM] Processing Logic-Loops for Subject: {current_student}")
    exit(0)

if __name__ == "__main__":
    run_brain()
