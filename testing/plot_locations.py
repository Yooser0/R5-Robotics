import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

#Load the 'positions.csv' file
log_path = os.path.join(os.path.dirname(__file__), 'flight_logs/flight_6/positions.csv')
positions = pd.read_csv(log_path)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = []
y = []
z = []
barometric = []

for i in range(0, len(positions)):
    #Get the x, y, and z coordinates
    x.append(positions['x'][i])
    y.append(positions['y'][i])
    z.append(positions['barometric'][i]-positions['barometric'][0])
    # barometric.append(positions['barometric'][i]-positions['barometric'][0])

#Plot the x, y, and z coordinates
ax.scatter([x[0]], [y[0]], [z[0]], 'red')
ax.text(x[0], y[0], z[0], 'Start')
ax.scatter([x[-1]], [y[-1]], [z[-1]], 'blue')
ax.text(x[-1], y[-1], z[-1], 'End')

ax.plot3D(x, y, z, 'green')
# plt.plot(range(0,len(barometric)), barometric)
#Show the plot
plt.show()


