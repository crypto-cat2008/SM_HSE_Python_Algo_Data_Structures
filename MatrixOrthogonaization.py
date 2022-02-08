import numpy as np
import numpy.linalg as LA
import math

def gs_cofficient(a, b):
    denominator = np.dot(b, b)
    if denominator == 0:
        return 0
    return np.dot(a, b) / np.dot(b, b) # getting the coefficient for each b_i


def gs_process(A):
    B = []
    for i in np.arange(A.shape[0]):
        a_i = A[i]
        for b in B:
            proj_vec = gs_cofficient(a_i, b) * b
            a_i = a_i - proj_vec
        B.append(a_i)
    return np.array(B)

# example use - vector equal row
A = np.array([[-1/math.sqrt(63),1,-2,-1], [1/math.sqrt(63),1,0,0],[-2/math.sqrt(63),0,1,0], [-1/math.sqrt(64),0,0,1]])

basis = gs_process(A)
print("Orthogonal basis:\n", basis, '\n')


# to normalize the basis:
def normalize(X):
    return np.array([x / LA.norm(x)
                     if LA.norm(x) != 0
                     else np.zeros(len(x))
                     for x in X])


normalized = normalize(basis)
print("Orthonormal basis:\n", normalized, '\n')