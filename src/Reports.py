
"""
NTF2 Flux Analysis through NPC model
All rights reserved.

Developed by: Sanjeev Kumar Gautam
Date: 2025

Description:
    This script processes LAMMPS trajectory data to compute:
	1. Net translocation count of NTF2s through the Nuclear Pore Complex (NPC) over time.
	2. Number of NTF2s within the central channel (z ∈ [-200, 200]) over time.

Output Files:
	- Count_from0_wkapB.txt: Net upward translocations
	- Count_in_pore_wkapB-brush.txt: Count in central pore region
"""

import sys
from Globals 	import *
import 	math 

#@timer
def Report(frames, total_frames, central_atoms):

    """
    Analyzes trajectory data to compute:
    - Net translocation counts
    - Molecule counts in central z-region (brush region)
    Outputs results to .txt files.
    """

    print("Total Central Atoms:", central_atoms)
    FF = gl.NO_FRAMES[0]  # Number of frames in the first dump file
    out1 = open('../run/Count_from0_wkapB.txt', 'w')
    out2 = open('../run/Count_in_pore_wkapB.txt', 'w')
    # Temporary arrays to store unwrapped z-coordinates
    m, n = [0]*15000, [0]*15000
    passed = 0

    for i in range(total_frames):
        if i > 5:
            for j in range(central_atoms):
                m[j] = frames[str(i-1)]["iz"][j]
                n[j] = frames[str(i)]["iz"][j]
                if n[j] - m[j] > 0:  # Positive displacement = net upward translocation
                    passed += 1
        # Adjust time based on chunk index
        time_val = ((i* 50000/30000)*0.0009 if i <= FF else (i - FF + (FF * 50000 / 30000)) * 0.0009)
        out1.write(f"{i}\t{time_val:.5f}\t{passed}\n")

    for i in range(total_frames):
        count_pore = 0
        for j in range(central_atoms):
            z = frames[str(i)]["z"][j]
            if gl.ENTRY_z < z < gl.EXIT_z:  # Inside central pore region
                x, y = frames[str(i)]["x"][j], frames[str(i)]["y"][j]
                dist = math.sqrt(x**2 + y**2)
                if dist < 183.4:  # Inside cylindrical brush region
                    count_pore += 1
        time_val = ((i* 50000/30000)*0.0009 if i <= FF else (i - FF + (FF * 50000 / 30000)) * 0.0009)
        out2.write(f"{i}\t{time_val:.5f}\t{count_pore}\n")

    out1.close()
    out2.close()

