import os
import sys
import glob

from slicer import slicer

# Variables
frame_rate = 10;        # Number of slices
nprocs = 16;
variables = ["u", "v", "p"]

# Open solution of heaving foil of delFI
path = os.getcwd()
solpath = path + "/solution_error/visit_error_000000.mfem_root"



# Create compute engine
OpenComputeEngine("localhost", ("-np", str(nprocs)))

# Create slices
slicer(variables, frame_rate, False, solpath, True, "error")

# Stop script
sys.exit()
