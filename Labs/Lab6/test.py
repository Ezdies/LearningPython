import time
import numpy as np

xin = range(10 ** 6)
t = time()
xout = []

for i in xin:
    xout.append(i ** 2)

print(time()-t)

t = time()

xout = [i ** 2 for i in xin]
print(time() - t)

t= time()

xout = list(map(lambda i: i**2, xin))

print(time() - t)

t = time()

xout = list(map((2).__rpow__, xin))

print(time - t) 

t = np.array([1,2,3,4,5])
t0 = np.zeros(10)
t1 = np.ones(10)

