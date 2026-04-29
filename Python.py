import os
import sys

def run_reaction_audit():
    # The Robot Teacher looks for the reaction type
    # ELI5: +1 means 👍 was clicked!
    reaction = os.getenv('REACTION_TYPE', '')
    
    print(f"🔎 [AUDIT] Scanning Node for Reaction: {reaction}")
    
    if reaction == "+1":
        print("✅ MASTERY CONFIRMED: Architect provided a Thumbs Up (👍).")
        sys.exit(0) # Green Checkmark
    elif reaction == "-1":
        print("❌ AUDIT FAILED: Architect provided a Thumbs Down (👎).")
        sys.exit(1) # Red X
    else:
        print("⚠️ STANDBY: Waiting for Architect reaction...")
        sys.exit(1)

if __name__ == "__main__":
    run_reaction_audit()
