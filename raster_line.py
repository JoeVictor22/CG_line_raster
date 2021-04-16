import numpy as np
import matplotlib.pyplot as plt
import math
import time

# line limits
x1, y1 = 0, 0
x2, y2 = 9, 3

size_matrix = 10

# matrix resolution
res = (size_matrix, size_matrix)

# creating the matrix
matriz = np.zeros(res)

dX = x2 - x1
dY = y2 - y1

m = dY/dX
b = y1 - (m*x1)

'''
if dX > dY:
    # 1 pra coluna
else:
    # 1 pra linha
'''

def grava(x, y):
    matriz[round(x)][round(y)] = 1


grava(x1,y1)

if dX > dY:
    while(x1 < x2):
        x1 += 1
        y = m * x1 + b
        grava(x1, y)
else:
    while (y1 < y2):
        y1 += 1
        x = (y1-b)/m
        grava(x, y1)

print(matriz.T[::-1])
plt.matshow(matriz.T[::-1])
