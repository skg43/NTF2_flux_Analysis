
"""
NTF2 Flux Analysis
All rights reserved.

Developed by: Sanjeev Kumar Gautam
Date: 2025

Description:
    Parses center of mass coordinates of NTF2 molecules from multiple LAMMPS trajectory files 
    to analyze their passage through a Nuclear Pore Complex (NPC) model. 
    Implements flux calculations by detecting molecule crossings across defined boundaries.
"""

import	sys
from Globals     import *


def parse_frame(framescount, startline, endline, file_index):
				OTHER_ATOMS = gl.N_Nup + gl.N_Wall + (gl.N_Kap * gl.AA_Kap)
				
				resid = OTHER_ATOMS + gl.NTF2_CENTER  # Atom ID of the first NTF2 central residuepol_dp_wkapB-noBS.txt"
				data = {"fc": [], "id": [], "Resid": [], "x": [], "y": [], "z": [], "iz": []}
				with open(f"../dump/dump-prod-ntf2-{file_index}.lmp", 'r') as f:
						lines = it.islice(f, startline, endline)
						for line in lines:
								parts = line.split()
								if int(parts[0]) == resid:
								# Store frame count and coordinates for each central atom
										data["fc"].append(framescount)
										data["id"].append(int(parts[0]))
										data["Resid"].append(int(parts[1]))
										data["x"].append(float(parts[3]))
										data["y"].append(float(parts[4]))
										data["z"].append(float(parts[5]))
										data["iz"].append(float(parts[8]))  # Unwrapped z coordinate
										resid += gl.AA_NTF2  # Move to next NTF2 molecule (center separated by 246 atoms)
										
				print(f"Loaded frame {framescount+1} from dump-prod-ntf2-{file_index}.lmp")
				return data
				
print("....")

@timer
def Load_all_Frames():
    """
    Loads all frames from all dump files in parallel using a ProcessPoolExecutor.
    Returns: 
        frames (dict): keyed by frame index with extracted atom data
        total_frames (int): total number of frames processed
        central_atoms (int): number of NTF2s (should be same across all frames)
        
    """
		
    TotAA_NTF2= int(gl.N_NTF2) * int(gl.AA_NTF2)
    Other_AAs = (gl.N_Nup + gl.N_Kap*gl.AA_Kap + gl.N_NTF2*gl.AA_NTF2)
    
    total_frames = sum(gl.NO_FRAMES)
    all_data = {}
    workers = [None] * total_frames

    with cf.ProcessPoolExecutor() as executor:
        current_frame = 0
        for file_index, frame_count in enumerate(gl.NO_FRAMES):
            startline = gl.H_lines
            for i in range(frame_count):
                # First file has extra lines, adjust chunk size accordingly
                endline = startline + (Other_AAs if file_index == 0 else TotAA_NTF2)
                
                workers[current_frame] = executor.submit(parse_frame, current_frame, startline, endline, file_index)
                startline = endline + gl.H_lines
                current_frame += 1

        for i in range(total_frames):
            all_data[str(i)] = workers[i].result()
    

    return all_data, total_frames, len(all_data['0']['id'])


