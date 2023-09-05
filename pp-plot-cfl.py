import pandas as pd
import matplotlib.pyplot as plt
import os

# Open data
path = os.getcwd()
path = path + "/output.0.dat" 
data = pd.read_csv(path, delim_whitespace=True, skiprows=[0,2])

# Set headers correctly as they are shifted upon the import, delete the last column
headers = data.columns.values
data.drop(data.columns[len(data.columns)-1], axis=1, inplace=True)
col_rename_dict = {i:j for i,j in zip(headers[0:-1], headers[1:])}
data.rename(columns=col_rename_dict, inplace=True)
headers = data.columns.values


# Plot residuals
fig, axs = plt.subplots(1)
x = data['time'].to_numpy()
y = data['cfl'].to_numpy()
axs.plot(x, y)  
axs.set_ylabel('cfl')
axs.set_xlabel('time')
plt.savefig('pp-cfl.pdf', bbox_inches='tight')
plt.close()

