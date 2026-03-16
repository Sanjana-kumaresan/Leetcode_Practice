class Solution(object):
    def decodeString(self, s):
        stack, n, a = [], 0, ""
        for c in s:
            if c.isdigit():
                n = n*10 + int(c)
            elif c == '[':
                stack.append((a,n))
                a,n = "", 0
            elif c == ']':
                prev, k = stack.pop()
                a = prev + a*k
            else:
                a += c
        return a            