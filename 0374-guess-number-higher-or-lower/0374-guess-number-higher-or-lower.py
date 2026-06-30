class Solution(object):
    def guessNumber(self, n):
        low = 0
        high = n
        while low <= high:
            mid = (low + high ) // 2
            res = guess(mid)
            if res < 0:
                high = mid - 1
            elif res > 0:
                low = mid + 1
            else:
                return mid    