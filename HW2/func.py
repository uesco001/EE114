#!/user/bin/python

import random
##  Generates random bits as boolean values #
def BitGenerator(N):
    array = []
    for i in range(0,N):
        array.append( .5 < random.random()  )
    return array

#  Decodes the arra 
# encoding transmission and decoding happens all herey
def Decoding(p,N,R,array):
    ret_array = []            # creats return array
    for i in range(0,N):      # 0 - N to go through Bits
        bit_result = 0        # stores the majotiy 
        for j in range(0,R):  # 0 - R to simulate R independent events of possible flipping
            if(p > random.random()):        # if random variable is with in p then it should be flipped
                bit_result += -1        # decrementing represents a flip
            else:
                bit_result += 1         # incrementing represnts non flip

        if(bit_result > 0):             # R should be odd
            ret_array.append(array[i])  # if bit result was positive then the  majority did not flip 
        else:
            ret_array.append(not array[i]) # if bit_result was negative then the majority flipped 

    return ret_array

def Success(p,N,R):
    array = BitGenerator(N)         # generates random array of boolean
    new_array = Decoding(p,N,R,array)  # generates decoded array 
    if array == new_array:          # returl 1 if successful transmission 0 if not         
        return 1           
    else:
        return 0

