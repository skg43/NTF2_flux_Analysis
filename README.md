# NTF2 Flux Analysis

This project analyzes the molecular flux of Nuclear Transport Factor 2 (NTF2) through a Nuclear Pore Complex (NPC) model using LAMMPS simulation outputs. It parses center of mass coordinates from multiple trajectory files and calculates molecular flux by detecting crossings through defined regions.

## Project Description

Selective molecular transport through the Nuclear Pore Complex (NPC) is crucial for regulating nucleocytoplasmic exchange.  
This project models the passage of NTF2 molecules through an NPC model by:

- Parsing center of mass coordinates from LAMMPS output files.
- Tracking molecules crossing predefined boundaries.
- Calculating flux and generating summary reports.
- Automating the full analysis pipeline using Python scripting.

The analysis is implemented in Python and demonstrates scalable processing of large simulation datasets.

## Repository Structure

```
NTF2_flux_Analysis/
├── input.inp           # Input file specifying analysis parameters
├── dump/               # LAMMPS output files (trajectories)
├── run/                # Shell script, output logs, and analysis results
├── src/                # Python source code for parsing, calculation, and reporting
│   ├── CalcFlux.py
│   ├── Flux.py
│   ├── Globals.py
│   ├── ReadInput.py
│   ├── Reports.py
│   └── run.py
└── README.md           # Project overview and usage instructions
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/NTF2_flux_Analysis.git
   cd NTF2_flux_Analysis
   ```

2. Prepare the input files:
   - Place `input.inp` in the project root.
   - Place LAMMPS trajectory files (`dump-prod-*.lmp`) inside the `dump/` folder.

3. Run the analysis:
   ```bash
   cd run
   bash run.sh
   ```

4. Output files will be saved in the `run/` directory.

## Skills and Tools Demonstrated

- Python programming for scientific data analysis
- Molecular dynamics data parsing (LAMMPS output)
- Molecular flux computation and time-series analysis
- Multiprocessing for performance optimization
- Shell scripting for workflow automation
- Git and GitHub for version control and project management

## License

This project is licensed under the MIT License.

## Developed By

Sanjeev Kumar Gautam
