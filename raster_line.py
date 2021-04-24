import numpy as np
import matplotlib.pyplot as plt
import math
import time
from pprint import pprint

def drawPoint(x, y):
    matriz[x][y] = 1

# line limits

# line examples
x1, y1 = 2, 2
x2, y2 = 2, 20


# ignores direction
'''
x1, x2 = sorted((x1,x2))
y1, y2 = sorted((y1,y2))
'''
# determine max size
size_matrix = max(x1, x2, y1, y2)

# matrix resolution
res = (size_matrix, size_matrix)

# creating the matrix
matriz = np.zeros(res)

dX = x2 - x1
dY = y2 - y1

# if dX or dY is zero, m = 0, else m = dY/dX
m = dY/dX if dX and dY else 0

b = y1 - (m*x1)


# dX > dY
# dY > dX
# dX == dY
# dX == 0 or dY == 0


if abs(dX) > abs(dY):
    xi, xf = sorted((x1, x2))

    while xi < xf:
        yi = int(round(m * xi + b))
        drawPoint(xi, yi)
        xi += 1
else:
    yi, yf = sorted((y1, y2))

    while yi < yf:
        try:
            xi = int(round((yi - b) / m))
        except ZeroDivisionError:
            xi = x1

        drawPoint(xi, yi)
        yi += 1


pprint(matriz)

matriz = matriz.T[::-1]
plt.imshow(matriz)
plt.colorbar()
plt.show()
