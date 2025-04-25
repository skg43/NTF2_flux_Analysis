#!/usr/bin/python3

"""
NTF2 Flux Analysis through NPC model
All rights reserved.

Developed by: Sanjeev Kumar Gautam
Date: 2025

Description:
    Core module implementing the molecular flux tracking algorithms and data structures.
"""

from ReadInput   import *
from Globals     import *
from CalcFlux import *
from Reports   import *

gl.version = "22 September 2025"

def Flux():
   prm = ReadInput()
   print("Input read!!!")
   gl_def(prm)
   frames, total_frames, central_atoms = Load_all_Frames()
   print("...")
   print("Writing output...")
   print("...")
   Report(frames, total_frames, central_atoms)
   print("Output Written!!")
   
