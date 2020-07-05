from functools import reduce

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        need = {1,2,3,5}            
        j = 1
        count = 0
        # ans = []    
        while count<=n:
            s = set(reduce(list.__add__, 
                    ([i, j//i] for i in range(1, int(j**0.5) + 1) if j % i == 0)))
            if(j not in need):
                s.remove(j)
                s.remove(1)

            if(s.issubset(need) and len(s)!=0):
                count += 1
                # ans.append(j)
                need.add(j)
            if(count==n):
                return j
            j += 1
            



        