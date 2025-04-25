
"""
NTF2 Flux Analysis through NPC model
All rights reserved.

Developed by: Sanjeev Kumar Gautam
Date: 2025

Description:
    Defines global variables and constants used throughout the flux analysis project.
"""

import 	sys
from 	math import *
import itertools as it
import concurrent.futures as cf
import os
import time
from functools import wraps


class gl:

	"""
	Defines data structures and methods for tracking molecule positions and flux events.
	"""

	ENTRY_z= None
	EXIT_z= None
	N_nup= None
	N_wall= None
	N_Kap= None
	N_NTF2= None
	AA_Kap= None
	AA_NTF2= None
	NO_FRAMES= None
	version= None



def gl_def(prm):

#***************************************************
#
#				Simulation parameters
#
#***************************************************
	gl.ENTRY_z = prm[0]
	gl.EXIT_z = prm[1]
	gl.N_Nup = prm[2]
	gl.N_Wall = prm[3]
	gl.N_Kap = (prm[5] if prm[4]==1 else 0)
	gl.AA_Kap = prm[6]
	gl.N_NTF2 = prm[7]	
	gl.AA_NTF2 = prm[8]
	gl.NO_FRAMES = prm[9:]

#***************************************************
#
#				global settings
#
#***************************************************


	gl.H_lines = 9 # number of lines of the header section
	gl.NTF2_CENTER = 224  # Center of Mass bead in NTF2 molecule




def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)   # Call the function
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' finished in {elapsed_time:.2f} seconds")
        return value
    return wrapper_timer
	

