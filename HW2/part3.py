#!/user/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random
import math
import sys
from func import BitGenerator, Decoding, Success
trials = 1000
#######################################################
#                NUMBER 3                             #
#######################################################i

N = [ 30, 100, 300, 1000]
count = [ 0, 0, 0, 0 ]
R = 9
p = 0.1
Psucc = [ [] for i in range(len(N))]

for i in range(trials):
    for j in range(len(N)):
        count[j] += Success(p,N[j],R)
        Psucc[j].append(float(count[j])/(i+ 1))

Psuccess = []
for i in range(len(N)):
    Psuccess.append(Psucc[i][trials-1])

plt.figure(1)

plt.subplot(2,2,1)
plt.plot(Psucc[0])
plt.title('P(M = M*) as func. of trials when N = 30')
plt.xlabel('trials')
plt.ylabel('probability')


plt.subplot(2,2,2)
plt.plot(Psucc[1])
plt.title('P(M = M*) as func of trials when N = 100')
plt.xlabel('trials')
plt.ylabel('probability')


plt.subplot(2,2,3)
plt.plot(Psucc[2])
plt.title('P(M = M*) as func of trials when N = 300')
plt.xlabel('trials')
plt.ylabel('probability')


plt.subplot(2,2,4)
plt.plot(Psucc[3])
plt.title('P(M = M*) as func of trials when N = 1000')
plt.xlabel('trials')
plt.ylabel('probability')

plt.tight_layout( )

plt.figure(2)
plt.plot(N,Psuccess,marker=".")
plt.title('P(M = M*) as func of N')
plt.ylabel('probability')
plt.xlabel('N (number of bits)')
ax = plt.gca()
ay = plt.gca()
ax.set_yticks(Psuccess)
ax.set_xticks(N) 

plt.show()
