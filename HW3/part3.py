#!/user/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random 
import math
from time import sleep
from func import MEAN,VAR,COR,BINARISE



FP = open('adult.data', 'r')
data = []
for line in FP:
    data.append(line.split(", "))

num_rows = len(data)
num_columns = len(data[0])



age = [] 
workclass = []
fnlwgt = []
education = []
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
    education.append(data[i][3])
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

        
workclassD = [ "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"]
educationD = [ "Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th", "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"  ]
marital_statusD = [ "Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"]
occupationD = [ "Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv", "Armed-Forces"] 
relationshipD = ["Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"]
raced = [ "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"]
sexd = ["Female","Male"]
native_countryD = [ "United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany", "Outlying-US(Guam-USVI-etc)", "India", "Japan", "Greece", "South", "China", "Cuba", "Iran", "Honduras", "Philippines", "Italy", "Poland", "Jamaica", "Vietnam", "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic", "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala", "Nicaragua", "Scotland", "Thailand", "Yugoslavia", "El-Salvador", "Trinadad&Tobago", "Peru", "Hong", "Holand-Netherlands" ]

discrete = [ [workclass,workclassD] , [education, educationD] ,[marital_status, marital_statusD] ,[occupation,occupationD],[relationship, relationshipD],[race,raced],[sex,sexd],[native_country, native_countryD] ] 
discreteD = [ "workclass", "education","marital status","occupation","relationship","race", "sex","native_country"]



for d in range(len(discrete)): 
    print("CORRELATION OF",discreteD[d], "\n")
    for i in range(len(discrete[d][1])):
        print("correlation between income and",discrete[d][1][i],"is",COR(above_50,BINARISE( discrete[d][0] , discrete[d][1][i] ))) 

    print('\n')




