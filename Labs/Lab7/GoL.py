import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

grid_size = 50
Z = np.random.rand(grid_size, grid_size)
Z[Z>0.5] = 1
Z[Z!=1] = 0

grids = []

for i in range(0, grid_size):
    for j in range(0, grid_size):
        grid = Z[i:i+3, j:j+3]
        grids.append(grid)

fig, ax = plt.subplots()
mat = ax.matshow(Z)

def update(frame):
    mat.set_data(grids[frame])
    return [mat]

ani = FuncAnimation(fig, update, frames=len(grids), interval=50)

plt.show()

