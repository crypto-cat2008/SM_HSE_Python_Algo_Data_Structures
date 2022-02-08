import numpy as np
import numpy.linalg as la
import math
from sklearn.decomposition import PCA

from sympy import Matrix

#  A = np.array([[-2, 1, 1], [1, -1, 2], [-1, 3, -1]])
#  B = np.array([[-1, 2, 0], [2, 1, 2], [3, 2, 1]])
#  v = np.array([[2], [-1], [3]])

# Rank
#  print('Rank A:', LA.matrix_rank(A), sep='\n')

# Matrix Multiplication
#  print('Multiplication A and B', np.dot(A, B), sep='\n')

# Multiplication by Vector
#  print('Multiplication A by vector v', np.dot(A, v), sep='\n')

# The reduced row echelon form
#  a = Matrix(A)
#  print('Echelon form', a.rref(), sep='\n')

# Matrix Inverse
#  inv = la.inv(A)
# print('A inverse', inv, sep='\n')

# Transpose A
#  print('Transpose A', np.transpose(A), sep='\n')

# Identity
#  identity = np.identity(3)
#  print('Identity', identity)

# Eigenvalues and eigenvectors
# w, v = la.eig(A)

# Determinant
# det = la.det(A)

# Inner product
# b = np.inner(a, c)

# QR decomposition
# Q, R = la.qr(A)

# Column by row multiplication
# A = np.array([1,2,3])
# AT = A.T
# print(np.outer(A.T, A))

# SVD
# A = np.array([[1,2,-1], [2,4,-2]])
# U, S, VT = la.svd(A)
# print(U, '\n', S, '\n', VT, '\n')
# print(np.transpose(VT))


# Week 6

A = np.array([[1,2,-1], [2,4,-2]])
U, S, VT = la.svd(A)

# print(U, '\n', S, '\n', VT, '\n')
# print(np.transpose(VT))


# task 1
A = np.array([1,2,3])
AT = A.T
# print(np.sum(np.outer(A.T, A)))


# task 1

U = np.array([[-2/math.sqrt(5), -1/math.sqrt(5), 0], [-1/math.sqrt(5),2/math.sqrt(5),0], [0,0,1]])
Sigma = np.array([[5,0],[0,0],[0,0]])
V = np.array([[-1/math.sqrt(5), -2/math.sqrt(5)], [-2/math.sqrt(5), 1/math.sqrt(5)]])

# print(U@Sigma@V.T)

U = np.array([[0,-1,0], [-1,0,0], [0,0,1]])
Sigma = np.array([[5,0],[0,0],[0,0]])
V = np.array([[-0.6,-0.8], [-0.8, 0.6]])

# print(U@Sigma@V.T)

A = np.array([[4,-1],[-1,4]])


# SGA2
# Task 1

A = np.array([[0,0], [-2,1]])
B = np.array([[1,-8/5], [0,-1/5]])
BI = la.inv(B)
#print(BI)
# print(A@BI)
C = np.array([[0,0],[-2,11]])
# print(C@B)

# task 2

A = np.array([[2,1,2], [-2,-1,-2],[4,2,4],[2,1,2]])
AT = np.transpose(A)
B = AT@A
# print(B)
w, v = la.eig(B)
#print(w, v)

U = np.array([[-1/math.sqrt(63),1,-1,-0.167], [1/math.sqrt(63),1,1,0.167], [-2/math.sqrt(63),0,1,-0.33],[1/math.sqrt(63),0,0,1]])
Sigma = np.array([[math.sqrt(63), 0,0],[0,0,0],[0,0,0],[0,0,0]])
VT = np.array([[-2,-1,-2],[3/math.sqrt(2), 0, -3/math.sqrt(2)], [1/math.sqrt(2), -4/math.sqrt(2),1/math.sqrt(2)]])

#print(U@Sigma@VT)

# task 3
A = np.array([[0,0,1/2,1/3],[0,1,0,1/3],[1/2,0,0,0],[1/2,0,1/2,1/3]])
B = np.ones((4,4))
#print(np.multiply(0.85,A))
#print(np.multiply(0.15/4,B))
C = np.multiply(0.85,A) + np.multiply(0.15/4,B)
# print(C)

# task 4
A = np.array([[0.73,0.12,0.1], [0.15,0.73,0.2],[0.12,0.15,0.7]])
p1 = np.array([[9400],[500],[100]])
p2 = A@p1
print(p2)
p3 = A@p2
print(p3)
p4 = A@p3
print(p4)






























