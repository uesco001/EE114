#!/user/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random 
import math

import sys

def BitGenerator(N,R):
    array = []
    bit = False 
    for i in range(0,N):
        bits = .5 < random.random()
        array.append([bits for i in range(R)  ]  )
    return array

p = float(input("Input probability p  "))

N = int(input("Input number of bits N   "))

R = int(input("Input number encoding R   "))

arrays = BitGenerator(N,R)

print(arrays)



