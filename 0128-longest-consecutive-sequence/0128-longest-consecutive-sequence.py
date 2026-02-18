class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        a = sorted(set(nums))
        count = 1
        max_count = 1
        for i in range(1, len(a)):
            if a[i] == a[i-1] + 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        return max(max_count, count)