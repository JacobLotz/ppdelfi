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
labels = ['mom x it :','mom y it :', 'mass it :', 'mom x it 0', 'mom y it 0', 'mass it 0']
headers = ['res_u', 'res_v', 'res_p', 'res_u_0', 'res_v_0', 'res_p_0']
for var, label in zip(headers, labels):
	x = data['time'].to_numpy()
	y = data[var].to_numpy()
	axs.plot(x, y, label = label)  
axs.set_yscale('log')
axs.set_ylabel('||res||')
axs.set_xlabel('time')
plt.legend(loc="upper right", ncol=3)
plt.savefig('pp-residuals.png', bbox_inches='tight')
plt.close()

