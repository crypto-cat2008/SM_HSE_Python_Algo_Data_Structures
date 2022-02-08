import numpy as np
a = np.array([[1, 0, 2], [2, -1, 0], [0, 1, 0]])
b = np.array([[0, 2], [1, 3], [1, 0]])
c = np.array([[0, -2, 2], [1, 0, 0]])

at = a.transpose()
bt = b.transpose()
ct = c.transpose()

r1 = np.dot(np.dot(c,at),b)
r2 = np.dot(np.dot(bt,a),ct)
r = r1 - r2
print(r)

c = np.array([1,2,1,2])
b = np.array([[0,2,1,3], [-1,0,6,4], [1,0,1,-7], [0,7,0,1]])
ct = c.transpose()
print(np.dot(ct,c))

r = np.dot(np.dot(ct, c), b)
print(r)

a = np.array([[2,-4],[-1,1]])
b = np.array([[2,3],[1,2]])
c = np.array([[-4,1],[-3,1]])

r = np.dot(np.dot(a, b), c)
print(r)