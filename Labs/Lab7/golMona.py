import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


grid_size = 20

Z = np.random.rand(grid_size, grid_size)

Z[Z>0.5] = 1
Z[Z != 1] = 0

def anim(frame, Z):
    new_Z = np.zeros((grid_size, grid_size))
    for i in range(1, grid_size-1):
        for j in range(1, grid_size-1):
            count = np.sum(Z[i-1:i+2, j-1:j+2]) - Z[i,j] #sąsiedzi dookola i,j

            if Z[i,j] == 1 and (count < 2 or count > 3):
                new_Z = 0
            elif Z[i,j] == 0  and count == 3:
                new_Z[i,j] = 1
            else:
                new_Z[i,j] = Z[i,j]
    mat.set_data(new_Z)
    Z[:] = new_Z[:]
    return [mat]


fig, ax = plt.subplots()
mat = ax.matshow(Z, cmap = "plasma")


anim = FuncAnimation(fig, anim,  frames = 200, interval = 10)

plt.show()