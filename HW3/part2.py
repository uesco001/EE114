#!/user/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random 
import math
from time import sleep
from func import MEAN,VAR,COR



FP = open('adult.data', 'r')
data = []
for line in FP:
    data.append(line.split(", "))

num_rows = len(data)
num_columns = len(data[0])



age = [] 
workclass = []
fnlwgt = []
edu = []
edu_num = []
marital_status = []
occupation = []
relationship = []
race = []
sex = []
capital_gain = []
capital_loss = []
hpw = []
native_country = []
above_50 = []

for i in range(num_rows):
    age.append( int(data[i][0]) )
    workclass.append(data[i][1])
    fnlwgt.append( int(data[i][2]) )
    edu.append(data[i][3])
    edu_num.append( int(data[i][4]) )
    marital_status.append(data[i][5])
    occupation.append(data[i][6])
    relationship.append(data[i][7])
    race.append(data[i][8])
    sex.append(data[i][9])
    capital_gain.append( int(data[i][10]) )
    capital_loss.append( int(data[i][11]) )
    hpw.append( int(data[i][12]) )
    native_country.append(data[i][13])
    if( data[i][14][0] == ">" ):
        above_50.append(1)
    else:
        above_50.append(0)

cont = [ age , fnlwgt, edu_num, capital_gain, capital_loss, hpw]
cont_name =  [ "age" , "fnlwgt", "education number", "capital gain", "capital loss", "hours per week"] 

for i in range(len(cont)):
    print("correlation between",cont_name[i],"and income is ", COR(above_50,cont[i]),"\n")




