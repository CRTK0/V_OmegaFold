from pymol import cmd

def extract_ptp1b_target():
    # 1. Clean the virtual environment
    cmd.reinitialize()
    print("[V_OmegaFold] Initiating extraction of metabolic target (PTP1B)...")

    # 2. Download the real human crystallographic structure (PDB ID: 1SUG)
    cmd.fetch('1sug', 'Target_PTP1B')
    
    # 3. Show surface to visualize actual topology
    cmd.show_as('surface', 'Target_PTP1B')
    cmd.color('gray70', 'Target_PTP1B')
    
    # 4. IDENTIFY THE WEAK POINT: Cysteine 215
    # This exact residue is the "blade" PTP1B uses to cut the insulin signal
    cmd.select('destructive_core', 'Target_PTP1B and resi 215')
    cmd.color('red', 'destructive_core')
    
    # 5. Aesthetics and Focus
    cmd.set('transparency', 0.2, 'Target_PTP1B')
    cmd.show('spheres', 'destructive_core')
    cmd.zoom('destructive_core')
    
    print("\n=================================================")
    print("[!] TARGET ACQUIRED: HUMAN PTP1B ENZYME.")
    print("[!] CRITICAL ANCHOR POINT MARKED IN RED (Cysteine 215).")
    print("=================================================")

if __name__ == "__main__":
    # Execute the extraction
    extract_ptp1b_target()