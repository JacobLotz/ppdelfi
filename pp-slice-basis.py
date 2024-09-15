import os
import sys
import glob

from slicer import slicer

# Variables
frame_rate = 10;        # Number of slices / second
nprocs = 32;

# Create compute engine
OpenComputeEngine("localhost", ("-np", str(nprocs)))

"""
Velocity
"""
# Open solution of heaving foil of delFI
path = os.getcwd()
solpath = path + "/visit_Basis_u/" 
variables = ["u"]
####
basis_p = glob.glob(solpath + 'visit_Basis_u_000000.mfem_root')[0]
slicer(variables, frame_rate, True, basis_p, True, "basis_u_0")

#####
basis_p = glob.glob(solpath + 'visit_Basis_u_000001.mfem_root')[0]
slicer(variables, frame_rate, True, basis_p, True, "basis_u_1")

#####
basis_p = glob.glob(solpath + 'visit_Basis_u_000002.mfem_root')[0]
slicer(variables, frame_rate, True, basis_p, True, "basis_u_2")


# Open solution of heaving foil of delFI
path = os.getcwd()
solpath = path + "/visit_Basis_v/" 
variables = ["u"]
####
basis_p = glob.glob(solpath + 'visit_Basis_v_000000.mfem_root')[0]
slicer(variables, frame_rate, True, basis_p, True, "basis_v_0")

#####
basis_p = glob.glob(solpath + 'visit_Basis_v_000001.mfem_root')[0]
slicer(variables, frame_rate, True, basis_p, True, "basis_v_1")

#####
basis_p = glob.glob(solpath + 'visit_Basis_v_000002.mfem_root')[0]
slicer(variables, frame_rate, True, basis_p, True, "basis_v_2")

"""
Pressure
"""
# Open solution of heaving foil of delFI
path = os.getcwd()
solpath = path + "/visit_Basis_p/" 
variables = ["u"] # u = p

#####
basis_p = glob.glob(solpath + 'visit_Basis_p_000000.mfem_root')[0]
slicer(variables, frame_rate, True, basis_p, True, "basis_p_0")

#####
basis_p = glob.glob(solpath + 'visit_Basis_p_000001.mfem_root')[0]
slicer(variables, frame_rate, True, basis_p, True, "basis_p_1")

#####
basis_p = glob.glob(solpath + 'visit_Basis_p_000002.mfem_root')[0]
slicer(variables, frame_rate, True, basis_p, True, "basis_p_2")

# Stop script
sys.exit()