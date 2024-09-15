import os
import sys
import glob

from slicer import slicer

# Variables
frame_rate = 15;        # Number of slices
nprocs = 16;
#variables = ["u", "v", "p","vmag"]
#variables = ["p","vmag"]
#variables = ["vmagvec", "vorticityvec"]
variables = ["vorticityvec"]

# Open solution of heaving foil of delFI
path = os.getcwd()
solution = path + "/solution_rom/visit_rom_000000.mfem_root" 


# Create compute engine
OpenComputeEngine("localhost", ("-np", str(nprocs)))

# Create slices
slicer(variables, frame_rate, True, solution, True)

# Stop script
sys.exit()
