class Solution(object):
    def plusOne(self, digits):
        num = int("".join(str(i) for i in digits))
        ans = [int(x) for x in str(num+1)] 
        return ans
        