class Solution(object):
    def isNumber(self, s):
        return bool(match(r'[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$',s))