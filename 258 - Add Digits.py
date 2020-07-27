class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        ans = sum(list(map(int, str(num))))%9
        if ans==0:
            return 9
        return ans