#!/user/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random
import math
import sys
from func import BitGenerator, Decoding, Success
trials = 1000


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
