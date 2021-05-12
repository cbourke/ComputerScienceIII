import sys
import math
from array import *
import numpy as np

n = int(sys.argv[1])
k = int(sys.argv[2])

P=[[0 for i in range(k+1)] for j in range(n+1)] # initialize
             
for i in range(n+1):
    for j in range(k+1):
        if j == 0 or i == j:
            P[i][j] = 1
        else:
            P[i][j] = P[i-1][j-1] + P[i-1][j]

r = P[n][k]

print(str(n) + " choose " + str(k) + " = " + str(r))

