import numpy as np
from fractions import Fraction
import math


clist = []
dlist = []
dlist.append([0,0,0,0])

#set "crazy" to a number whose square determines how many operations this thing actually does
crazy = 500
for a in range(1,crazy):
  for b in range(1,crazy):
    if( a != b ):
      c = b * (a+b)/(a-b)
      if (c.is_integer()):
        if(c > 0):
          div = math.gcd(math.gcd(int(a),int(b)),int(c))
          clist.append([0,int(a),int(a+b),int(a+b+c)])

clist.sort(key=lambda x: x[1])

dlist=list(set(map(tuple,map(sorted,clist))))
dlist.sort(key=lambda x: x[3])

elist = set()

for i in range(0,len(dlist)):
  div = int(math.gcd(math.gcd( int(dlist[i][1]), int(dlist[i][2])), int(dlist[i][3])))
  a = int(dlist[i][1]/div)
  b = int(dlist[i][2]/div)
  c = int(dlist[i][3]/div)
  elist.add((0,a,b,c))

elist = list(elist)
elist.sort(key=lambda x: x[3])


print(elist)
