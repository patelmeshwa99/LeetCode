class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c = x^y
        c = list("{0:b}".format(c))
        return c.count('1')
