import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation


# Thermal properties and dimensions

alpha = 111  # Thermal diffusivity ,I used the value of copper from wikipedia in this link https://en.wikipedia.org/wiki/Thermal_diffusivity
Lx, Ly = 152, 152  # Plate dimensions (mm)

# Number of nodes in each dimension (that the number of nodes that fdm will use to solve the heat equation)
N = 50
dx = Lx / (N - 1)
dy = Ly / (N - 1)

# Stability condition for dt
# I used the stability condition from this video https://www.youtube.com/watch?v=CXOrkQs4WYo
# Actually dx,dy are the same so we can use any of them (it's general for any change in the dimensions)
dt = min(dx**2, dy**2) / (4 * alpha)
time = 15  # Simulation duration in seconds
time_steps = int(time / dt)

# Discretize space and initialize temperature
Xvec = np.linspace(0, Lx, N)
Yvec = np.linspace(0, Ly, N)
X, Y = np.meshgrid(Xvec, Yvec)

T = np.full((N, N), 25.0)  # Initial temperature
T[:, 0] = T[:, -1] = T[0, :] = T[-1, :] = 200.0  # Boundary conditions

# Storage for temperature at each time step
Tout = np.zeros((time_steps, N, N))
Tout[0] = T

# Time-stepping loop
for t in range(1, time_steps):
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            # Calc dt_dy and dt_dx by Finite difference method (central difference)
            dt_dx = (T[i + 1, j] - 2 * T[i, j] + T[i - 1, j]) / dx**2
            dt_dy = (T[i, j + 1] - 2 * T[i, j] + T[i, j - 1]) / dy**2
            T[i, j] += alpha * dt * (dt_dx + dt_dy)
    Tout[t] = T

# Plotting and animation
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set_xlabel('x axis (mm)')
ax.set_ylabel('y axis (mm)')
ax.set_zlabel('Temperature (C)')
ax.set_xlim(0, Lx)
ax.set_ylim(0, Ly)
ax.set_zlim(0, 200)

# Initial surface plot
surface = [ax.plot_surface(X, Y, Tout[0], cmap=cm.jet)]

# Update function for animation


def update(frame):
    global surface
    surface[0].remove()
    surface[0] = ax.plot_surface(X, Y, Tout[frame], cmap=cm.jet)


# Create and save animation
animation = FuncAnimation(
    fig, update, frames=range(0, time_steps, 10), interval=50)
animation.save("heat_equation_3d_simulation.mp4", writer="ffmpeg")

plt.show()
