import numpy as np

a = 6
b = 6

matrix = [[i for i in range(a)] for j in range(b)]
c = np.array(matrix)
print('Matrix:\n', c)

