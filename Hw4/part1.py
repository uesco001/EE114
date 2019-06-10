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
h = []
fx = np.linspace(-3,3,6000)
for i in range(4):
    X.append( Zarray(mean,var,nn[i]))
    plt.figure(i)
    h.append(plt.hist(X[i],range=[-3,3],bins=np.arange(min(X[i]), max(X[i]) + binwidth, binwidth ), density = True))
    hh = plt.plot(fx, x1,lw = 2)
    plt.xticks(size = 20)
    plt.yticks(size = 20)
    plt.title('Pdf of Zn for n ='+ str(nn[i]),size =20)



print(h[3])

