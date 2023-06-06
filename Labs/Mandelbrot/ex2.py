import mplcatppuccin
import matplotlib as mpl
import matplotlib.pyplot as plt
from time import time
import numpy as np

a = np.ones((3, 3))
b = 2 * np.ones((2,3))
c = 5 * np.ones((3, 2))

np.vstack((a, b))
np.hstack((a, c))

matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(matrix)
print(matrix[0:2][0:2])
print(matrix[:1])
print(matrix[1:3, ::2])

matrix2 = np.array([[i * j for i in range(1, 21)] for j in range(1,11)])
print(matrix2)

n = 5
s = matrix2.shape
scat = [matrix2[:, i*s[1]//n:(i+1)*s[1]//n] for i in range(n)]
print(scat)
