class Solution:
    def reverseBits(self, n: int) -> int:
        num = '{:032b}'.format(n)
        l=list(num)
        l.reverse()
        s = "".join(l)
        return int(s, 2)