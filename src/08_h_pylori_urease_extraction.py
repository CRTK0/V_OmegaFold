"""
V_OmegaFold: H. Pylori Urease Extractor
Purpose: Downloads and isolates the Urease enzyme (PDB: 1E9Y).
Objective: Map the structural mold that allows H. pylori to survive stomach acid.
"""

import os
import urllib.request
import Bio.PDB

def fetch_and_isolate_urease():
    pdb_id = "1E9Y"
    output_dir = "outputs"
    raw_file = os.path.join(output_dir, f"{pdb_id}_raw.pdb")
    target_file = os.path.join(output_dir, "HP_Urease_Target.pdb")

    os.makedirs(output_dir, exist_ok=True)

    print(f"[V_OmegaFold] Extracting H. pylori Urease (PDB: {pdb_id})...")

    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    try:
        urllib.request.urlretrieve(url, raw_file)
        print(f"[+] Download complete.")
    except Exception as e:
        print(f"[!] Error: {e}")
        return

    parser = Bio.PDB.PDBParser(QUIET=True)
    structure = parser.get_structure(pdb_id, raw_file)
    
    class UreaseSelect(Bio.PDB.Select):
        def accept_chain(self, chain):
            # Isolating the primary catalytic chain
            return chain.get_id() == 'A'
            
        def accept_residue(self, residue):
            return residue.get_id()[0] == ' '

    io = Bio.PDB.PDBIO()
    io.set_structure(structure)
    io.save(target_file, UreaseSelect())

    print(f"\n[+] EXTRACTION SUCCESSFUL")
    print(f"[+] Target saved at: {target_file}")
    print("[!] Proceed to Column Scanner (05_column_locator.py).")

if __name__ == "__main__":
    fetch_and_isolate_urease()