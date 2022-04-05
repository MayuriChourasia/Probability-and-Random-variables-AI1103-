'''Mayuri Rajesh Chourasia
   BT21BTECH11001
   Graph plotting'''
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-14, 14)
m, c = 7/8,43/8
y=(m*x)+ c
plt.plot(x,y,linewidth=2,color='orange',label='8y-7x=43')
m,c=-8/7,6/7
y=(m*x)+c
plt.plot(x,y,linewidth=2,color='cyan',label='7y+8x=6')
# x axis values
x = [3,-1,6]
# corresponding y axis values
y = [8,2,-6]
# plotting the points
for i in range(0,3):
  plt.plot(x[i],y[i],marker='.', markerfacecolor='magenta', markersize=15)
plt.plot([0,0],[-10,10], linewidth=0.5, color='grey' )
plt.plot([-14,14],[0,0], linewidth=0.5, color='grey' )
for i in range(-14,14):
  plt.plot([i,i],[-14,14], linewidth=0.3, color='grey' )
  plt.plot([-14,14],[i,i], linewidth=0.3, color='grey' )
for i in range(-10,14,5):
  plt.plot([i,i],[-14,14], linewidth=0.7, color='grey' )
  plt.plot([-14,14],[i,i], linewidth=0.7, color='grey' )

plt.annotate('  A (3,8)',(3,8))
plt.annotate('  B (-1;2)',(-1,2))
plt.annotate('  C (6,-6)',(6,-6))
# setting x and y axis range
plt.ylim(-10,10)
plt.xlim(-13.5,13.5)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Question8(B)')
plt.legend()
# function to show the plot
plt.show()
