import numpy as np
from numpy import linalg as LA
from numpy import random as RN 

#Total number of Students.
#Sample size
N =40 

#Generating Events
#X=0 represents number of Girls.
#X=1 represents number of Boys.
x = RN.randint(0, high = 2, size=N)

#Finding the number of 1's and 0's obtained from above step.
obt_0 = np.count_nonzero(x==0)
obt_1 = N - obt_0

print("Randomn Probabilities:", obt_0/N, obt_1/N)
