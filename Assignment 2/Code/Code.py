'''
Mayuri CHourasia
BT21BTECH11001
'''
#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA

#Input matrix
A = np.array(([1,1,1],[2,5,7],[2,1,-1]))
b = np.array([9,52,0])
Ainv = LA.inv(A)
x = Ainv@b
print(12*Ainv,x,A@x)

x= np.reciprocal(x)

print('x =',x[0])
print('y =',x[1])
print('z =',x[2])

'''
OUTPUT:
[[ 36.  -6.  -6.]
 [-48.   9.  15.]
 [ 24.  -3.  -9.]] [1. 3. 5.] [ 9. 52.  0.]
x = 1.0
y = 0.3333333333333333
z = 0.2
'''
