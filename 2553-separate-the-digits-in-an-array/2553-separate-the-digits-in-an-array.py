class Solution(object):
    def separateDigits(self, nums):
        return [int(ch) for num in nums for ch in str(num)]
        