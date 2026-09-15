# Plotting Without Line
# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
import numpy as np
import matplotlib.pyplot as plt

x_axis = np.array([21, 45])
y_axis = np.array([4, 5])
plt.plot(x_axis, y_axis, 'o')
plt.show()

# ====================================================================================

# Multiple Points
# You can plot as many points as you like, just make sure you have the same number of points in both axis.

xaxis = np.array([1,4,6,19])
yaxis = np.array([3,8,1,10])
plt.plot(xaxis, yaxis)
plt.show()

# ====================================================================================

# Default X-Points
# If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.
# So, if we take the same example as above, and leave out the x-points, the diagram will look like this:

ypoints = np.array([3, 8, 14, 6, 8, 6])
xpoints = np.array([2, 9, 7, 6, 7, 9])
plt.plot(ypoints)
plt.plot(xpoints)   
plt.show()

# ====================================================================================