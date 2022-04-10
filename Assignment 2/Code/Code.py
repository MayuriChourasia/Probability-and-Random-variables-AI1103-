'''
Mayuri CHourasia
BT21BTECH11001
'''
# Importing Library
import numpy as np

def inverse(arr):
    # Finding an inverse of given array
    inverse_array = np.linalg.inv(arr)
    return(inverse_array)

# Function to multiply two matrices
def multmatrice(A,B):
    matrix=[]
    result = [[0],[0],[0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    for r in result:
        matrix.append(r)
    return matrix        
    
#taking the co-efficient matrix and the constant matrix as inputs
coeff_mat = np.array([[1, 1, 1],
				[2, 5, 7],
				[2, 1, -1]])
const_mat = np.array([[9],[52],[0]])

inv_mat = inverse(coeff_mat)                    #coeff_mat = co-efficient matrix
                                                #const_mat = constant matrix
fin_mat = multmatrice(inv_mat,const_mat)        #inv_mat = inverted matrix
                                                #fin_mat = final matrix
a=int(fin_mat[0][0])                             
b=int(fin_mat[1][0])                            
c=int(fin_mat[2][0])

x=1/a
y=1/b
z=1/c

print('Solution for the given system of equations is:')
print('x =',x )
print('y =',y)
print('z =',z)

'''
OUTPUT:

Solution for the given system of equations is:
x = 1.0
y = 0.3333333333333333
z = 0.2


** Process exited - Return Code: 0 **
Press Enter to exit terminal

'''
