#!/user/bin/python

import numpy as np
import matplotlib.pyplot as plt
import random 
import math

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Number 1 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def Distance(P1,P2):
     return math.sqrt( (P1.x - P2.x)**2 + (P1.y - P2.y)**2 )
 
class Point:
     def __init__(self):
         self.x = round(random.random(),4)
         self.y = round(random.random(),4)

N = 100000
X = []
binwidth = .01

for i in range(N):
     X.append(Distance(Point(),Point()))
plt.figure(0)
h = plt.hist(X,bins=np.arange(0,math.sqrt(2) + binwidth, binwidth),histtype='stepfilled',density=True)
plt.ylabel('probability(in percengtage)',size = 20)
plt.xlabel('distance between two points',size = 20)
plt.xticks(size = 20)
plt.yticks(size = 20)
plt.title('Probability of distance',size =20)


# *************** part two of one*************
plt.figure(1)
Pn = []
cnt = 0

for i in range(N):
     if(X[i] > .5):
          cnt = cnt + 1
     Pn.append(float(cnt)/(i+1))

plt.plot(Pn)

plt.ylabel('probability',size = 20)
plt.xlabel('N-number of trials',size = 20)
plt.xticks(size = 20)
plt.yticks(size = 20)
plt.title('P(A) v N',size = 20)
print("P(A) is around ", Pn[N-1])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Number 2 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
X2 = []
for i in range(N):
     P1 = Point()
     P2 = Point()
     P3 = Point()
     D1 = Distance(P1,P2)
     D2 = Distance(P2,P3)
     D3 = Distance(P1,P3)
     X2.append(min(D1,D2,D3))

plt.figure(2)
hist2 = plt.hist(X2,bins=np.arange(0,math.sqrt(2) + binwidth, binwidth),histtype='stepfilled',density=True)

plt.ylabel('probability(in percengtage)',size = 20)
plt.xlabel('distance between two points',size = 20)
plt.xticks(size = 20)
plt.yticks(size = 20)
plt.title('Probability of distance of three',size =20)
#*********************Part 2 of #2****************

plt.figure(3)
Pn2 = []
cnt = 0

for i in range(0,N):
     if(X2[i] > .5):
          cnt = cnt + 1
     Pn2.append(float(cnt)/(i+1))

plt.plot(Pn2)

plt.ylabel('probability',size = 20)
plt.xlabel('N-number of trials',size = 20)
plt.xticks(size = 20)
plt.yticks(size = 20)
plt.title('P(A) v N',size = 20)
print("P2(A) is around ", Pn2[N-1])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Number 3 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cnt = 0
X_d = [[0 for i in range(N)]]
for d in range(0,5):
         X_d.append( [round( random.random(),4) for i in range(N) ] )

Y_d = [[ 0 for i  in range(N) ]]
P_d = [ [0] for i in range(5)] 

for d in range(1,6):
     Y_d.append(Y_d[d - 1]) 
     for i in range(0,N-1):
         Y_d[d][i] += X_d[d][i] 
         if(Y_d[d][i] <= 1):
              cnt += 1
         P_d[d - 1].append( round(float(cnt)/(i+1),4) )
     cnt = 0

for i in range(0,5):
     print(P_d[i][N-1])
         
plt.show()
