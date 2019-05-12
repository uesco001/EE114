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
#                NUMBER 2                             #
#######################################################i
trials = 1000
succ_num = 0
N = 10
R = 9
p = 0.1

for n in range(trials):
    succ_num += Success(p,N,R)
print('probabilty for\nN =',N,'\nR =',R,'\np =',p,'\nis ',succ_num/float(trials))
