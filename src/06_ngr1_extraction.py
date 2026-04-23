"""
V_OmegaFold: Neuro-Target Extractor
Purpose: Downloads and isolates the Human Nogo Receptor 1 (NgR1) - PDB: 1OZN.
Objective: Prepare the "Structural Mold" to block the paralysis signal post-stroke.
"""

import os
import urllib.request
import Bio.PDB

def fetch_and_isolate_ngr1():
    pdb_id = "1OZN"
    output_dir = "outputs"
    raw_file = os.path.join(output_dir, f"{pdb_id}_raw.pdb")
    target_file = os.path.join(output_dir, "NgR1_Target.pdb")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    print(f"[V_OmegaFold] Initiating extraction of Neuro-Target: {pdb_id} (NgR1)...")

    # 1. Download the raw structure from the RCSB Protein Data Bank
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    try:
        urllib.request.urlretrieve(url, raw_file)
        print(f"[+] Download complete: {pdb_id}")
    except Exception as e:
        print(f"[!] Error downloading PDB: {e}")
        return

    # 2. Parse and Clean the Structure (Remove water, keep only the receptor chain)
    print("[!] Cleaning structure... Isolating the main receptor chain.")
    parser = Bio.PDB.PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, raw_file)
    
    class ReceptorSelect(Bio.PDB.Select):
        def accept_chain(self, chain):
            # We only want the primary chain (usually 'A' or the largest one)
            return chain.get_id() == 'A'
            
        def accept_residue(self, residue):
            # Strip out water (HOH) and heteroatoms (ligands/salts from crystallization)
            return residue.get_id()[0] == ' '

    io = Bio.PDB.PDBIO()
    io.set_structure(structure)
    io.save(target_file, ReceptorSelect())

    print(f"\n=================================================")
    print(f"[+] EXTRACTION SUCCESSFUL")
    print(f"[+] Clean mold saved at: {target_file}")
    print(f"=================================================")
    print("[!] Ready for Column Scanning (Anomaly 31-121 Radar).")

if __name__ == "__main__":
    fetch_and_isolate_ngr1()