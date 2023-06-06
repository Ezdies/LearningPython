import mplcatppuccin
import matplotlib as mpl
import matplotlib.pyplot as plt
from time import time
import numpy as np
x=np.arange ( -2 ,1.01 ,.01)
y=np.arange ( -1.5 ,1.51 ,.01)
x,y=np.meshgrid(x,y)
z=x+1j*y
s=z.shape 
t = time()
z0 = np.copy(z)
res = 255 * np.ones(s)

for i in range (255):
    res[np.abs(z)>2] = i
    z = z**2 +z0

print(time()-t)
plt.imshow(res)
plt.show()