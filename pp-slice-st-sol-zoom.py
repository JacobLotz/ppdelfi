import os
import sys
import glob

from slicer import slicer

# Variables
n_slice = 5;        # Number of slices
nprocs = 1;
variables = ["u", "v", "p"]

# Open solution of heaving foil of delFI
path = os.getcwd()
solpath = path + "/solution/" 

# Find last solutionfile
listsolutions = glob.glob(solpath + 'visit_*.mfem_root') # * means all if need specific format then *.csv
lastsolution = max(listsolutions, key=os.path.getctime)

# Create compute engine
OpenComputeEngine("localhost", ("-np", str(nprocs)))

# Create slices
slicer(variables, n_slice, True, lastsolution)

# Stop script
sys.exit()
