'''Mayuri Rajesh Chourasia
   BT21BTECH11001
   Graph plotting'''
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
plt.close('all')
# Triangle 1
x=np.array([3,-1,6,3])
y=np.array([8,2,-6,8])
# Figure and Axes
fig1=plt.figure(1)
ax1=fig1.add_subplot(111)
# Plot Triangle 1 
ax1.axis('square')
plt.plot(x,y,color='green')
x = np.arange(-14, 14)
m, c = 7/8,43/8
y=(m*x)+ c
plt.plot(x,y,linewidth=2,color='orange',label='8y-7x=43')
m,c=-8/7,6/7
y=(m*x)+c
plt.plot(x,y,linewidth=2,color='cyan',label='7y+8x=6')
x = [3,-1,6]
y = [8,2,-6]
# plotting the points
for i in range(0,3):
  plt.plot(x[i],y[i],marker='.', markerfacecolor='magenta', markersize=15)
plt.annotate('  A (3,8)',(3,8))
plt.annotate('  B (-1;2)',(-1,2))
plt.annotate('  C (6,-6)',(6,-6))
# Axes Limits
plt.xlim([-10,10])
plt.ylim([-10,10])
# Grid
plt.grid(axis='both',which='major',color='grey', linestyle='-', linewidth=0.6)
plt.minorticks_on()
plt.grid(axis='both',which='minor',color='grey', linestyle='-', linewidth=0.2)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Question8(B)')
plt.legend()
plt.show()
