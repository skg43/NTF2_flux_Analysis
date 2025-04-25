#!/usr/bin/python3

"""
NTF2 Flux Analysis through NPC model
All rights reserved.

Developed by: Sanjeev Kumar Gautam
Date: 2025

Description:
    Main driver script to read inputs, initialize parameters, and execute the flux analysis workflow.
"""

global version
version = "2 May 2025"

from Flux	import *

@timer
def main():
	Flux()

if __name__ == '__main__':
	main() # Entry point for running the flux analysis

