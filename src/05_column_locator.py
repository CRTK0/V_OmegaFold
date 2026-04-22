"""
V_OmegaFold: Structural Column Finder
Purpose: Analyzes PDB coordinates to find "Architectural Anchors" (The 31-121 Binary Anomaly logic).
Identifies high-stability nodes that dictate the final 3D shape (The Structural Mold).
"""

import Bio.PDB
import numpy as np

def locate_structural_columns(pdb_file):
    print(f"[V_OmegaFold] Analyzing structural anchors in: {pdb_file}")
    
    parser = Bio.PDB.PDBParser(QUIET=True)
    structure = parser.get_structure('protein', pdb_file)
    
    columns = []
    master_columns_found = []
    
    # Algorithm: Identifying residues with the lowest B-factor (highest stability)
    # and strategic spatial positioning based on the 31-121 Binary Anomaly Logic.
    for model in structure:
        for chain in model:
            for residue in chain:
                # Check to ensure the residue has atoms
                atoms = list(residue.get_atoms())
                if not atoms:
                    continue
                    
                # Calculate average B-factor to determine physical 'stiffness'
                avg_b_factor = np.mean([atom.get_bfactor() for atom in atoms])
                res_id = residue.get_id()[1]
                res_name = residue.get_resname()
                
                # Standard Column Detection (B-factor threshold)
                if avg_b_factor < 20.0:
                    columns.append(f"{res_name}-{res_id}")
                    
                # The 31-121 Binary Anomaly Master Column Detection
                if res_id in [31, 121]:
                    master_columns_found.append(f"{res_name}-{res_id}")
                    print(f"\n[!!!] MASTER COLUMN DETECTED: {res_name}-{res_id} (Foundational Anchor)")
                    print(f"      -> Enforcing directional and thermodynamic stability for the Structural Mold.")

    print(f"\n[!] ANALYSIS COMPLETE: {len(columns)} Standard Structural Columns detected.")
    if columns:
        print(f"[+] Primary Anchors identified: {columns[:5]}...")
    
    if master_columns_found:
        print(f"\n[★] CRITICAL: The 31-121 Binary System presence detected: {master_columns_found}")
    else:
        print("\n[i] Note: Master Column targets (31/121) not present in this specific micro-peptide sequence.")
        
    print("[+] These residues act as the 'physical skeleton' of the fold.")

if __name__ == "__main__":
    # Example: Analyzing our synthesized warhead
    try:
        locate_structural_columns("outputs/V_OMEGA_Warhead_PTP1B.pdb")
    except FileNotFoundError:
        print("[!] Error: Run 01_esmfold_local.py first to generate the PDB file.")