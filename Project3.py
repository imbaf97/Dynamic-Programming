import random
import math
import time
import numpy as np

n = int(input('Input numbers of point as n : '))
array = []
for i in range(0, n):
    array.append(random.randint(1, 100))
print('array is '+ str(array))

mc1sa = []  ##create an array, and we append mc1s[i] values to it.

# Computes mc1s[i] for all values of 1 <= i <= n. In this function, we introduce i rather than n, because it always ends at n.
def mc1s(l):
    #mc1s[i] = minimum cost to serve servers from i to n, using just one server.
    n = len(l)
    for i in range(1,n):
        for k in range(i,n):
            s = 0          ##s means sum of l[i]
            s += l [k]

        half = s/2      ## half means half of sum s.
        s1 = 0
        index = n-1   ## index is the location of sever, when weight is more than half.

        for k in range(i,n):  ## reverse
            s1 += l[k]
            if s1 >= half:
                break
            else:
                index -= 1
        s2 = 0
        for k in range(i,n):
            s2 += abs(k-index)*l[k]
        mc1sa.append(s2)
    print ('mc1sa is'+str(mc1sa))




# Computes mcks[j][k] for all combinations 1..j, using k servers
def mcks(array):
    l = array
    z = int(input('Input numbers of servers  as z : '))
    n = len(l)
    #l = []
    #for i in range(0, n):
        #l.append(random.randint(1, 100))
    mc1s(l)
    mcks = [[1000 for i in range(z)] for i in range(n)]

    for j in range(1,n):       # base step
        mcks[j][0] = 0


    mcks[0][1] = 0             # base step
    mcks[1][1] = min(l[0],l[1])# base step
    for j in range(n):
        for m in range(1,z+1):
            count = []
            for x in range(0,j-1):
                count.append( mcks[x][m-1] + mc1sa[x+1])
                #mcks[j][m] = min(count, mcks[j][m])

    print('mcks[j][m]for different x is' + str(count))
    m = min(count)
    print('when j is equal to' + str(n) +'  and there are'+ str(z)+ '  severs, most optimal answer is '+ str(m))


mcks(array)