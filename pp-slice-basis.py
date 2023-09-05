import os
import sys
import glob

from slicer import slicer

# Variables
n_slice = 30;        # Number of slices
nprocs = 1;

# Create compute engine
OpenComputeEngine("localhost", ("-np", str(nprocs)))

"""
Velocity
"""
# Open solution of heaving foil of delFI
path = os.getcwd()
solpath = path + "/visit_Basis_uv/" 
variables = ["u", "v"]

#####
basis_p = glob.glob(solpath + 'visit_Basis_uv_000000.mfem_root')[0]
slicer(variables, n_slice, True, basis_p, True, "basis_uv_0")

#####
basis_p = glob.glob(solpath + 'visit_Basis_uv_000001.mfem_root')[0]
slicer(variables, n_slice, True, basis_p, True, "basis_p_1")

#####
basis_p = glob.glob(solpath + 'visit_Basis_uv_000002.mfem_root')[0]
slicer(variables, n_slice, True, basis_p, True, "basis_p_2")


"""
Pressure
"""
# Open solution of heaving foil of delFI
path = os.getcwd()
solpath = path + "/visit_Basis_p/" 
variables = ["p"]

#####
basis_p = glob.glob(solpath + 'visit_Basis_p_000000.mfem_root')[0]
slicer(variables, n_slice, True, basis_p, True, "basis_p_0")

#####
basis_p = glob.glob(solpath + 'visit_Basis_p_000001.mfem_root')[0]
slicer(variables, n_slice, True, basis_p, True, "basis_p_1")

#####
basis_p = glob.glob(solpath + 'visit_Basis_p_000002.mfem_root')[0]
slicer(variables, n_slice, True, basis_p, True, "basis_p_2")

# Stop script
sys.exit()