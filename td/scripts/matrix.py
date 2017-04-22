import numpy as np
M = np.ones((4,4))
M[2,3] = 2
M[3,1] = 6
print(M)

M = np.diag([2, 3, 4, 5, 6], k=-1)
M = M[:, :5]
print(M)

M = np.tile([[4,3], [2, 1]], (2, 3))
print(M)
