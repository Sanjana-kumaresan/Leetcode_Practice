class Solution(object):
    def countKDifference(self, nums, k):
        c,n=0,len(nums)
        for i in range(n):
            for j in range(i,n):
                if abs(nums[i]-nums[j])==k:
                    c+=1
        return c
        