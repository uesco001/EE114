#!/user/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random 
import math


def Distance(P1,P2):
     return math.sqrt( (P1.x - P2.x)**2 + (P1.y - P2.y)**2 )
 
class Point:
     def __init__(self):
         self.x = round(random.random(),4)
         self.y = round(random.random(),4)

N = 1000
X = []
binwidth = .01

#for i in range(1,N):
#     X.append(Distance(Point(),Point()))

#h = plt.hist(X,bins=np.arange(0,math.sqrt(2) + binwidth, binwidth),histtype='stepfilled')
#plt.ylabel('probabiliy(in percengtage)',size = 50)
#plt.xlabel('distance between two points',size = 50)
#plt.xticks(size = 20)
#plt.yticks(size = 20)
#plt.title('Probability of distance')





# this is part two of one
Pn = []
cnt = 0

for i in range(1,N):
     for j in range(1,i):
          if(Distance(Point(),Point()) > .5):
               cnt = cnt + 1
     Pn.append(float(cnt)/i)
     cnt = 0
plt.plot(Pn)
plt.show()

