import numpy as np

sz = 1000
nv = np.loadtxt('../codes/gau.dat', dtype='double')
bv = np.loadtxt('../codes/ber.dat', dtype='double')
sig = (10**(0.5))*bv + nv
e0 = np.count_nonzero((sig < 0) & (bv > 0))
n0 = np.count_nonzero(bv > 0)
e1 = np.count_nonzero((sig > 0) & (bv < 0))
n1 = np.count_nonzero(bv < 0)
print("X = 1: ", e0/n0)
print("X = -1: ", e1/n1)