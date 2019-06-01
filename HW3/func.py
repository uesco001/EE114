#!/user/bin/python

import random
import math
##  Generates random bits as boolean values #
def MEAN(array):
    mean = 0.0
    N = len(array)
    for i in range(N):
        mean = array[i] + mean
    mean = mean / N 
    return N

def VAR(array, mean):
    var = 0.0
    N = len(array)
    for i in range(N):
        var = (array[i] - mean)**2 + var
    return var / N 

def COR(xarray,yarray):
    Nx= len(xarray)
    Ny = len(yarray)
    if( Ny != Nx):
        print("ERRORORRORORO")
        return -666
    MX = MEAN(xarray)
    MY = MEAN(yarray)
    stdx = math.sqrt(VAR(xarray,MX))
    stdy = math.sqrt(VAR(yarray,MY))
    numerator = 0.0
    for i in range(Nx):
        numerator = (xarray[i] - MX)*(yarray[i] - MY) + numerator
    return (numerator) / (Nx*stdy*stdx)
# return a binarised array to get correlation of something
def BINARISE(array,word):
    new_array = []
    N = len(array)
    for i in range(N):
        if(array[i] == word):
            new_array.append(1)
        else:
            new_array.append(0)
    return new_array




