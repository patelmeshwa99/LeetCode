'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        while(i<=n):
            n-=i
            i+=1
        return (i-1)
