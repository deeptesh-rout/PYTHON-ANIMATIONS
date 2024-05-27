import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Create figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data for a 3D helix
t = np.linspace(0, 4 * np.pi, 1000)
x = np.sin(t)
y = np.cos(t)
z = t

# Create a plot object
line, = ax.plot(x, y, z, lw=2)

# Set up the axes properties
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, 4 * np.pi])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Helix Animation')

# Function to update the plot
def update(num, x, y, z, line):
    line.set_data(x[:num], y[:num])
    line.set_3d_properties(z[:num])
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(t), fargs=(x, y, z, line), interval=20, blit=False)

# Save the animation as a GIF
ani.save('3d_helix_animation.gif', writer='imagemagick')

# Show the plot
plt.show()
