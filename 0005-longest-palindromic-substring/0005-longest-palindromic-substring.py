class Solution(object):
    def longestPalindrome(self, s):
        ans = ""
        for i in range(len(s)):
            for l, r in ((i, i), (i, i+1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1; r += 1
                ans = max(ans, s[l+1:r], key=len)
        return ans      