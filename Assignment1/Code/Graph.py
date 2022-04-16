'''Mayuri Rajesh Chourasia
   BT21BTECH11001
   Graph plotting'''

import numpy as np
import matplotlib.pyplot as plt

def line_dir(m,A,k1,k2):
  len = 10
  d = A.shape[0]
  x_AB = np.zeros((d,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

#Generate line points
def line_pt(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Obtaining perpendicular vector
def perp_vector(m):
  m[1],m[0] =m[0],-m[1]
  return m
    
\
plt.close('all')
# Figure and Axes
fig1=plt.figure(1)
ax1=fig1.add_subplot(111)
# Plot Triangle 1 
ax1.axis('square')

# Assigning the points
A = np.array([3, 8])
B = np.array([-1, 2])
C = np.array([6, -6])


# Plotting Sides of Triangle
xAB = line_pt(A,B)
xBC = line_pt(B,C)
xCA = line_pt(C,A)
plt.plot(xAB[0,:],xAB[1,:])
plt.plot(xBC[0,:],xBC[1,:])
plt.plot(xCA[0,:],xCA[1,:])

# Plot Line perpendicular to BC through A
m=(B-C)
m=perp_vector(m)
xA = line_dir(m,A,-0.3,2)
plt.plot(xA[0,:],xA[1,:],label='8y-7x=43')

# Annotating the points
tri_coords = np.vstack((A,B,C)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A(3,8)','B(-1,2)','C(6,-6)']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,(tri_coords[0,i], tri_coords[1,i]),textcoords="offset points",xytext=(0,10),ha='center')

# Other stuff on plot
plt.title("Question 8 B")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
# Axes Limits
plt.xlim([-10,10])
plt.ylim([-10,10])
# Grid
plt.grid(axis='both',which='major',color='grey', linestyle='-', linewidth=0.5)
plt.minorticks_on()
plt.grid(axis='both',which='minor',color='grey', linestyle='-', linewidth=0.15)
plt.legend()
plt.show()
