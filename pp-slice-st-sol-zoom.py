import os
import sys
import glob

from slicer import slicer

# Variables
frame_rate = 20;        # Number of slices
nprocs = 16;
#variables = ["u", "v", "p"]
#variables = ["u", "v", "p","vmag", "vmagvec"]
#variables = ["vmag"]
#variables = ["vmagvec", "p"]
#variables = ["p"]
#variables = ["vorticityvec", "p","vmag"]
variables = ["p"]

# Open solution of heaving foil of delFI
path = os.getcwd()
solpath = path + "/solution/" 

# Find last solutionfile
listsolutions = glob.glob(solpath + 'visit_*.mfem_root') # * means all if need specific format then *.csv
lastsolution = max(listsolutions, key=os.path.getctime)

#lastsolution = solpath = path + "/solution/visit_000000.mfem_root"

# Create compute engine
OpenComputeEngine("localhost", ("-np", str(nprocs)))

# Create slices
slicer(variables, frame_rate, False, lastsolution, True)

# Stop script
sys.exit()
