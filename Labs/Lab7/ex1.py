import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

point = ax.plot([], [], "ro")[0]

def anima(frame):
    x = frame
    y = 0
    point.set_data([x], [y])
    return point

animation = FuncAnimation(fig, anima, frames=np.arange(-10, 10, 0.2), interval = 50)
plt.show()