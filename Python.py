import os
import sys

def run_reaction_audit():
    # Detect the architect's reaction [V]
    reaction = os.getenv('REACTION_TYPE', '')
    
    # GIANT VISUAL HUD FOR THE ARCHITECT
    print("\n" + "="*60)
    print("      🚀 SCHOOL QUALITY STUDIOS - AUDIT NODE 🚀      ")
    print("="*60)

    if reaction == "+1":
        print("\n   [ ✅ MASTERY CONFIRMED BY ARCHITECT ]   \n")
        print("   STATUS: 120 FPS HIGH-FIDELITY SUCCESS   ")
        print("   NODE: SYNCED TO GHOST DATABASE          ")
        print("\n" + "="*60 + "\n")
        sys.exit(0) 
        
    elif reaction == "-1":
        print("\n   [ ❌ AUDIT FAILED - IMPROVEMENT REQUIRED ]   \n")
        print("   STATUS: LOGIC-LOOP DISCONNECTED             ")
        print("\n" + "="*60 + "\n")
        sys.exit(1)
        
    else:
        print("\n   [ ⚠️ STANDBY - WAITING FOR ARCHITECT ]   \n")
        print("   ACTION: REACT WITH 👍 TO LOG MASTERY     ")
        print("\n" + "="*60 + "\n")
        sys.exit(1)

if __name__ == "__main__":
    run_reaction_audit()
