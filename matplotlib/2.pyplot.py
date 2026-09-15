import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2, 3, 9])
ypoints = np.array([4, 2, 5])

plt.plot(xpoints, ypoints)
# Parameter 1 is an array containing the points on the x-axis. ==> horizontal axis.
# Parameter 2 is an array containing the points on the y-axis. ==> vertical axis.
plt.show()
