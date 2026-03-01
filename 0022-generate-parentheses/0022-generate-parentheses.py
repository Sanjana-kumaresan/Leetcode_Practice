class Solution(object):
    def generateParenthesis(self, n):
        out = []
        def back_track(par='', left=0,right=0):
            if len(par) == 2*n:
                out.append(par)            
            if left < n:
                back_track(par+'(', left+1,right)
            if right < left:
                back_track(par+')', left, right+1)         
        back_track()
        return out  