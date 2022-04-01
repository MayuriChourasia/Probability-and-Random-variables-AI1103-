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

def perpendicular_slope(arr2,arr3):
    s_perp=get_slope(arr2,arr3)[::-1]
    s_perp[1]=-(s_perp[1])
    return s_perp
    #slope of perpendicular= s_per[0]/s_perp[1]
    '''we have got the slope of the perpencicular, now we will buit a function to find the constant 
    in the general equation of line i.e. y=mx+c,using the co-ordinates of point through which 
    the line passes and the slope of the perpencicular'''

A=np.array([3,8])
B=np.array([-1,2])
C=np.array([6,-6])

#for the first subquestion
slope=[]
slope=get_slope(B,C)
print('i) The slope of line BC is:',slope[0],'/',slope[1],'\n')

#for the second subquestion
s=perpendicular_slope(B,C)
print('ii) The equation of line perpendicular to BC and passing')
'''For a line passing through a point (𝑥1,𝑦1) and having a slope m can be given 
   by the equation : ( y - 𝑦1) = m ( x - 𝑥1)'''
print('through the point A is given by:',s[1],'y -',s[0],'x  =',s[1]*A[1]- s[0]*A[0])

#end
