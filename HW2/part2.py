#!/user/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random
import math
import sys
from func import BitGenerator, Decoding, Success
trials = 1000
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
