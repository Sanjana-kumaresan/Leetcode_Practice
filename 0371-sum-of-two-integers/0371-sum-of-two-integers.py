class Solution(object):
    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            temp = (a ^ b) & mask
            b = ((a & b) << 1) & mask
            a = temp
        return a if a <= max_int else ~(a ^ mask)