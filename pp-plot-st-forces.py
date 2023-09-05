import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

from geomdl import BSpline
from geomdl import utilities
from geomdl.visualization import VisMPL


# evaluation delta
n = 80;
extrusion = 6.2832;

# Open data
path = os.getcwd()
path = path + "/stforcex.0.dat" 
data = pd.read_csv(path, delim_whitespace=True, skiprows=[0,1,2], header=None)

fx = []
for col in data.columns.values:
    fx.append(-1/extrusion*data[col].iloc[-1])

path = os.getcwd()
path = path + "/stforcey.0.dat" 
data = pd.read_csv(path, delim_whitespace=True, skiprows=[0,1,2], header=None)

fy = []
for col in data.columns.values:
    fy.append(-1/extrusion*data[col].iloc[-1])

# Create time vector
t_nonper = np.linspace(0,1,len(data.columns)+1)
t = t_nonper[0:-1]



# Create a curve for the drag
controlpoints = []

for i in range(0, len(fx)):
    controlpoints.append([t[i], fx[i]])
# periodicity
controlpoints.append([t_nonper[-1], fx[0]])


curvex = BSpline.Curve()
curvex.degree = 2
curvex.ctrlpts = controlpoints

curvex.knotvector = utilities.generate_knot_vector(curvex.degree, len(curvex.ctrlpts))# Auto-generate knot vector
curvex.sample_size = n # Set evaluation delta
curvex.evaluate() # Evaluate curve


# Create a curve for the lift
controlpoints = []

for i in range(0, len(fy)):
    controlpoints.append([t[i], fy[i]])
# periodicity
controlpoints.append([t_nonper[-1], fy[0]])


curvey = BSpline.Curve()
curvey.degree = 2
curvey.ctrlpts = controlpoints

curvey.knotvector = utilities.generate_knot_vector(curvey.degree, len(curvey.ctrlpts))# Auto-generate knot vector
curvey.sample_size = n # Set evaluation delta
curvey.evaluate() # Evaluate curve



# Plot Forces
fig, axs = plt.subplots(1)

axs.set_ylabel('force')
axs.set_xlabel('time')

ctrlpts = np.array(curvex.ctrlpts)
curvepts = np.array(curvex.evalpts)

plt.plot(ctrlpts[:, 0], ctrlpts[:, 1], color='black', linestyle='', marker='o', markersize='3')  # control points polygon
plt.plot(curvepts[:, 0], curvepts[:, 1],  linestyle='-', label = r"$C_D$")  # evaluated curve points color='blue'


ctrlpts = np.array(curvey.ctrlpts)
curvepts = np.array(curvey.evalpts)

plt.plot(ctrlpts[:, 0], ctrlpts[:, 1], color='black', linestyle='', marker='x', markersize='3')  # control points polygon
plt.plot(curvepts[:, 0], curvepts[:, 1], linestyle='-', label = r"$C_L$")  # evaluated curve points color='orange'
plt.legend()
plt.savefig('pp-st-forces.png', bbox_inches='tight')
plt.close();
