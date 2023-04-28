import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

scat = ax.plot(x, y)[0]


def anima(frame):
    y[:-1] = y[1:] ##przesuwa o jeden w prawo elementy tablicy
    y[-1] = np.sin(2*np.pi*frame/100)
    
    scat.set_data([x, y])


animation = FuncAnimation(fig, anima, frames=100, interval = 50)
plt.show()