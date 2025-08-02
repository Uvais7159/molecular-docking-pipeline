 Molecular Docking Automation Pipeline
This repository contains a Python-based automation pipeline for performing molecular docking of triazine-based hybrid compounds with the bacterial receptor S. aureus dihydrofolate reductase (DHFR, PDB ID: 3FRA) using AutoDock Vina.

The pipeline is designed to support computational drug discovery by streamlining the following tasks:

Ligand and protein preparation

Site-specific docking execution

Automated parsing of binding affinities

Batch processing of multiple compounds

🚀 Features
📁 Batch Docking of .pdbqt ligands

🎯 Fixed grid center based on 3FRA active site (x=26.587, y=14.104, z=43.568)

🧠 Binding affinity extraction for lead identification

📊 Results summary printed for quick review

 Folder Structure
 DockingPipeline/
├── docking_pipeline.py     # Main automation script
├── receptor/               # Contains 3FRA.pdbqt file
├── ligands/                # Place your compound .pdbqt files here
├── docking_results/        # Output folder with docking logs and poses
└── README.md               # Documentation
 Usage Instructions
 Install AutoDock Vina

Place .pdbqt ligands into the ligands/ folder

Place the receptor 3FRA.pdbqt into the receptor/ folder

Run the script:
python docking_pipeline.py
🧬 Applications
Structure-based drug design

Screening of bioactive heterocycles (e.g., triazine-coumarin-benzothiazole hybrids)

Evaluation of antibacterial potency based on docking scores

👨‍🔬 Author
Mohd Uvais Raza Khan
Integrated M.Sc. Chemistry | Researcher in Medicinal and Computational Chemistry
📬 Feel free to connect via GitHub or LinkedIn
