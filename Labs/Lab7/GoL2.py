import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

grid_size = 50
Z = np.random.rand(grid_size, grid_size)
Z[Z>0.5] = 1
Z[Z!=1] = 0

def evo(frame, Z, grid_size):
    Z_new = np.zeros((grid_size, grid_size))
    for i in range (grid_size):
        for j in range(grid_size):
            neigh = Z[i-1:i+2, j-1:j+2].sum() - Z[i,j]
            if Z[i, j] == 1 and neigh in {2, 3}:
                Z_new[i, j] = 1
            if Z[i, j] == 0 and neigh == 3:
                Z_new[i, j] = 1
    Z[:] = Z_new[:]
    mat.set_data(Z)
    return mat


fig, ax = plt.subplots()
mat = ax.matshow(Z)


anim =FuncAnimation(fig, evo,
                    frames=200, fargs=(Z, grid_size),
                    interval=10)


plt.show()

