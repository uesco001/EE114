#!/user/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random
import math
import sys
from func import BitGenerator, Decoding, Success
trials = 1000

#######################################################
#                NUMBER 4                             #
#######################################################i
p = .2
N = 100
P_succ_array = []
P_success = 0
R = 9
count = 0
while P_success <.9:
    count = 0
    for i in range(trials):
        count += Success(p,N,R)
    P_success = float(count)/trials
    P_succ_array.append(P_success)
    R += 1
print('R must be ',R, 'so Psuccess is >= .9')

count = 0
while P_success <.99:
    count = 0
    for i in range(trials):
        count += Success(p,N,R)
    P_success = float(count)/trials
    P_succ_array.append(P_success)
    R += 1

print('R must be ',R, 'so Psuccess is >= .99')

count = 0
while P_success <.999:
    count = 0
    for i in range(trials):
        count += Success(p,N,R)
    P_success = float(count)/trials
    P_succ_array.append(P_success)
    R += 1

print('R must be ',R, 'so Psuccess is >= .999')

count = 0
while P_success <.9999:
    count = 0
    for i in range(trials):
        count += Success(p,N,R)
    P_success = float(count)/trials
    P_succ_array.append(P_success)
    R += 1

print('R must be ',R, 'so Psuccess is >= .9999')
