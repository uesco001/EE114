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

for i in np.arange(-3,3,0.0345):
    x1.append( math.exp(-(i**2 / 2) ) / math.sqrt(2*math.pi))


binwidth = 0.02

nn = [1,2,4,8,16]
X = []
h = []
fx = np.linspace(-3,3,6000)
for i in range(5):
    X.append( Zarray(mean,var,nn[i]))
    h.append(plt.hist(X[i],range=[-3,3],bins=np.arange(min(X[i]), max(X[i]) + binwidth, binwidth ), density = True))
var1 = 0
GCDF=[]
for i in range(len(x1)):
    var1 = var1 + x1[i]
    GCDF.append(var)


MCDF = []
ZCDF = []
var2 = 0
for k in range(5):
    var2 = 0
    MCDF.append([])
    ZCDF.append([])
    for i in range(len(x1)):
        var2 = var2 + h[k][0][i]
        ZCDF[k].append(var2)
        MCDF[k].append(var2 - GCDF[i])
    plt.plot(MCDF[k], label='n = '+str(nn[k] ))
plt.legend()
plt.show()



