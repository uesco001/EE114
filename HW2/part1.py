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
#                NUMBER 1                             #
#######################################################i
while True:
    p = float(input("Input probability p  "))

    N = int(input("Input number of bits N   "))

    R = int(input("Input number encoding R   "))

    arrays = BitGenerator(N)
    new_array = Decoding(p,N,R,arrays)

    if(arrays == new_array):
        print('transmission success!')
    else:
        print('transmission failed')
