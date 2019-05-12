#!/user/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random
import math
import sys
trials = 1000

##  Generates random bits as boolean values #
def BitGenerator(N):
    array = []
    for i in range(0,N):
        array.append( .5 < random.random()  )
    return array

#  Decodes the array
def Decoding(p,N,R,array):
    ret_array = []
    for i in range(0,N):
        bit_result = 0
        for j in range(0,R):
            if(p > random.random()):
                bit_result += -1
            else:
                bit_result += 1

        if(bit_result > 0):
            ret_array.append(array[i])
        else:
            ret_array.append(not array[i])

    return ret_array

def Success(p,N,R):
    array = BitGenerator(N)
    new_array = Decoding(p,N,R,array)
    if array == new_array:
        return 1
    else:
        return 0

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
