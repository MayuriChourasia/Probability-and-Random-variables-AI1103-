'''Name:Mayuri Rajesh Chourasia
   Roll no: bt21btech1001'''

import numpy as np

def get_slope(arr2,arr3):
    slope=[]
    #difference in y co-ordinates
    slope.append(arr3[1]-arr2[1])
    #difference in x co-ordinates
    slope.append(arr3[0]-arr2[0])
    #slope=tan(theta) = (difference in y co-ordinates)/(difference in x co-ordinates)
    #slope=slope[0]/slope[1]
    return slope

A=np.array([3,8])
B=np.array([-1,2])
C=np.array([6,-6])

#for the first subquestion
slope=[]
slope=get_slope(B,C)
print('i) The slope of line BC is:',slope[0],'/',slope[1],'\n')

'''
OUTPUT:
i) The slope of line BC is: -8 / 7

'''
