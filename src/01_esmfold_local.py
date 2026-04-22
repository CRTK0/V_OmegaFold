import torch
from transformers import EsmForProteinFolding
import os
import time

def fold_peptide(sequence, output_filename):
    print("[V_OmegaFold] Initializing Offline Thermodynamic Engine...")
    print("[!] Hardware constraint check: Loading model to CPU...")
    
    # Load model directly from local cache (8.44GB offline execution)
    model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1", low_cpu_mem_usage=True)
    model = model.to("cpu")
    model.eval()

    print(f"\n[+] Folding synthetic sequence of {len(sequence)} residues: {sequence}")
    print("[!] Calculating free energies. Please wait...")

    start_time = time.time()

    # --- PHYSICAL COLLAPSE ---
    with torch.no_grad():
        pdb_output = model.infer_pdb(sequence)

    pdb_string = pdb_output[0] if isinstance(pdb_output, list) else pdb_output

    # --- EXPORT ---
    output_path = os.path.abspath(output_filename)
    with open(output_path, "w") as f:
        f.write(pdb_string)

    end_time = time.time()

    print(f"\n[+] SUCCESS. Thermodynamics resolved in {round(end_time - start_time, 2)} seconds.")
    print(f"[+] Protein materialized at: {output_path}")

if __name__ == "__main__":
    # The PTP1B Suicidal Inhibitor Warhead (De Novo Design)
    target_sequence = "EDDYFLVPR" 
    fold_peptide(target_sequence, "V_OMEGA_Warhead_PTP1B.pdb")