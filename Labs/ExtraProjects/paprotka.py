import numpy as np
import matplotlib.pyplot as plt


def paprotka(n):
    a = np.array([
    [[0.85, 0.04, 0], [-0.04, 0.85, 1.6]],
    [[-0.15, 0.28, 0], [0.26, 0.24, 0.44]],
    [[0.2, -0.26, 0], [0.23, 0.22, 1.6]],
    [[0, 0, 0], [0, 0.16, 0]]
])

    x = [0]
    y = [0]

    for i in np.random.choice([0, 1, 2, 3], size=n, p=[0.85, 0.07, 0.07, 0.01]):
        x.append(a[i][0][0] * x[-1] + a[i][0][1] * y[-1] + a[i][0][2])
        y.append(a[i][1][0] * x[-2] + a[i][1][1] * y[-1] + a[i][1][2])

    plt.figure(figsize=(6, 10))
    plt.plot(x, y, marker=".", linewidth=0, markersize=0.005)
    plt.show()

if __name__ == "__main__":
    paprotka(10000000)