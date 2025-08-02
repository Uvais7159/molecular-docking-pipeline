# Molecular Docking Automation Pipeline (AutoDock Vina + Python)
# Author: Uvais Raza
# Description: Automates docking of ligand with S. aureus DHFR receptor using AutoDock Vina

import os
import subprocess

# ---------- CONFIGURATION ----------
# Paths to AutoDock Vina and other tools
VINA_PATH = "/usr/local/bin/vina"  # Update to your Vina binary path
LIGAND_DIR = "ligands/"             # Directory containing ligand PDBQT files
OUTPUT_DIR = "docking_results/"     # Output folder
PROTEIN_PDBQT = "receptor/3FRA.pdbqt"  # Prepared receptor file

# Grid box settings for 3FRA
CENTER_X = 26.587
CENTER_Y = 14.104
CENTER_Z = 43.568
SIZE_X = 62
SIZE_Y = 62
SIZE_Z = 62

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------- FUNCTIONS ----------

def run_docking(ligand_file):
    ligand_name = os.path.basename(ligand_file).replace(".pdbqt", "")
    out_file = os.path.join(OUTPUT_DIR, f"{ligand_name}_out.pdbqt")
    log_file = os.path.join(OUTPUT_DIR, f"{ligand_name}_log.txt")

    command = [
        VINA_PATH,
        "--receptor", PROTEIN_PDBQT,
        "--ligand", ligand_file,
        "--center_x", str(CENTER_X),
        "--center_y", str(CENTER_Y),
        "--center_z", str(CENTER_Z),
        "--size_x", str(SIZE_X),
        "--size_y", str(SIZE_Y),
        "--size_z", str(SIZE_Z),
        "--out", out_file,
        "--log", log_file
    ]

    print(f"Docking {ligand_name}...")
    subprocess.run(command)
    print(f"Completed: {ligand_name}")

def extract_binding_energy(log_file):
    with open(log_file, 'r') as f:
        for line in f:
            if line.strip().startswith("1"):
                return float(line.split()[1])
    return None

# ---------- MAIN ----------
if __name__ == "__main__":
    results = []
    for file in os.listdir(LIGAND_DIR):
        if file.endswith(".pdbqt"):
            ligand_path = os.path.join(LIGAND_DIR, file)
            run_docking(ligand_path)

            log_path = os.path.join(OUTPUT_DIR, file.replace(".pdbqt", "_log.txt"))
            score = extract_binding_energy(log_path)
            results.append((file.replace(".pdbqt", ""), score))

    # Print summary
    print("\nDocking Summary:")
    for ligand, score in results:
        print(f"{ligand}: {score} kcal/mol")
