import numpy as np
#vectors
a = np.array([1, 4, 5])
b = np.array([-1, 4, 53])
c = a + b # c is vector (0, 8, 58 )
print("Vector sum", c)
d = a * b # d is vector (−1, 16, 265)
print("Elementwise vector product", d)

#arrays
m1 = np.array([[1, 4], [-5, 8]])
m2 = np.array([[7, -6], [-11, 2]])
# msum is array ([[8, −2], [−16, 10]])
msum = m1+m2
print("Matrix sum", msum)
# product is array ([[−37, 2], [−123, 46]])
product = np.dot(m1, m2)
print("Matrix product", product)

#zeros is a null matrix of shape 2x3
zeros = np.zeros((2,3))
print("Null matrix: ", zeros)
#i is an identity matrix of shape 3x3
i = np.identity(3)
print("Identity matrix: ", i)

#matrix inverse and multiplication
a = np.array([[-1, 3], [3, 5]])
b = np.array([[3], [7]])
inv = np.linalg.inv(a)
x = np.dot(inv, b)

from scipy.linalg import lu
B = np.array([[ 0, 0, 1], [0, 2, 2], [3, 0, 4]])
# PLU
P, L, U = lu(B)
# outputs true
print(np.allclose(np.dot(np.dot(P,L), U), B))

#Below is the example for 2D case
a = np.array([[1, 0], [0, 1]])
b = np.array([[4, 1], [2, 2]])
product = np.matmul(a, b) # also can be written as a @ b
print("Matrix product", product)

a = np.array([[1,2],[3,4]])
# sum_of_elements is 10
sum_of_elements = np.sum(a)
print("Sum of elements", sum_of_elements)

k = -9
abs_k = np.abs(k) #abs_k is 9
print("Absolute of -9 = ", abs_k)

# random matrix of size 4x4 with values from -15 to 15
m1 = np.random.randint(low=-15,high=15, size=(4, 4))
print("Original matrix", m1)
#replace all values that are greater than 0 with 1
filtered_m1 = np.where(m1 < 0, m1, -1)
print("Replacing non-negative values with -1", filtered_m1)