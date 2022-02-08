import numpy as np
import numpy.linalg as LA


A = np.array([[3,1,-2],
                [1,1,1],
                [-1,2,4]])
q, r = LA.qr(A)
print("Q=", q, '\n')
print("R=", r)
print(np.sum(r))
is_equal = np.allclose(A, np.dot(q,r))
print("Obtained the original matrix?", is_equal)