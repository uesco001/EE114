#!/user/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random 
import math
import scipy.stats as stats

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Number 1 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def GenerateX(n):
    return [ random.random() for i in range(n) ]

def Zn(mean,var,n):
     Sn = sum([random.random() for i in range(n)])
     return (Sn - n/2) / math.sqrt(n*var)


def Zarray(mean,var,n):
    z = []
    N = 1000000
    for i in range(N):
        z.append(Zn(mean,var,n))
    return z

mean = 1/2
var = 1/12
x1 = []

for i in np.arange(-3,3,0.001):
    x1.append( math.exp(-(i**2 / 2) ) / math.sqrt(2*math.pi))

binwidth = 0.02
nn = [1,2,4,8]
X = []
fx = np.linspace(-3,3,6000)
for i in range(4):
    X.append( Zarray(mean,var,nn[i]))

X.append(Zarray(mean,var,16))

q = 0
PP = []
for i in range(len(x1)):
    q = q + x1[i]
    PP.append(q)


YY = []
P = [[] for i in range(5)]
N = 1000000
for i in range(1):
    for j in range(N):
        y = 0
        for k in range(N):
            if(X[i][k] < j/N):
                y = y +1
        P[i].append(y/N)
        YY.append(P[i][j] - PP[j])
    plt.plot(YY)

plt.show()





