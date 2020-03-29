import random
import math
import numpy as np


# Computes mcks[j][k] for all combinations 1..j, using k servers
def mcks(l,n,z):

    mc1s = []   ##create an array, and we append mc1s[i] values to it.
                ## Computes mc1s[i] for all values of 1 <= i <= n. In this function, we introduce i rather than n, because it always ends at n.

    for i in range(1, n):
        for k in range(i, n):
            s = 0  ##s means sum of l[i]
            s += l[k]

        half = s / 2  ## half means half of sum s.
        s1 = 0
        index = i  ## index is the location of sever, when weight is more than half.

        for k in range(i, n):
            s1 += l[k]
            if s1 >= half:
                break
            else:
                index += 1
        s2 = 0
        for k in range(i, n):
            s2 += abs(k - index) * l[k]
        mc1s.append(s2)     ## mc1s[i] = minimum cost to serve servers from i to n, using just one server.

    mcks = [[1000 for i in range(n)] for i in range(n)]

    mcks[1][1] = mc1s[0]

    for j in range(0,n):
        for m in range(1,z+1):
            for x in range(1,j):
                count = mcks[x][m-1] + mc1s[x+1]
                mcks[j][m] = min(count, mcks[j][m])

    return mcks[n][z]

if __name__ == '__main__':
    n = int(input('Input numbers of point as n : '))
    z = int(input('Input numbers of point as z : '))
    l = []
    for i in range(0, n):
        l.append(random.randint(1, 10))
    print(l)

    mcks(l,n,z)
