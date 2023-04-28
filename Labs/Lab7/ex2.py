import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x, y = 0, 0
scat = ax.scatter(x, y) 

point = ax.plot([], [], "ro")[0]

def init():
    ax.set_xlim(0, np.pi*2)
    ax.set_ylim(-1.5, 1.5)

def anima(frame):
    x = frame
    y = np.sin(frame)
    scat.set_offsets([x, y])
    return point

animation = FuncAnimation(fig, anima, frames=np.linspace(0, 2*np.pi, 100), init_func=init, interval = 50)
plt.show()