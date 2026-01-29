class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            for a, b in [(i, i), (i, i+1)]:  
                while a >= 0 and b < len(s) and s[a] == s[b]:
                    a -= 1
                    b += 1
                if b - a - 1 > len(res):
                    res = s[a+1:b]
        return res
