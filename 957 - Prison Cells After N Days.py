import numpy
class Solution:
    def prisonAfterNDays(self, l, N):
        a=[0,0,0,0,0,0,0,0]
        i=1
        while(i<=N):
            a = [1 -abs(x1 - x2) for (x1, x2) in zip(numpy.roll(l,1), numpy.roll(l,-1))]
            a[0] = a[7] = 0
            l=a[:]
            i+=1
        return l