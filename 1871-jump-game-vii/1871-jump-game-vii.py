class Solution(object):
    def canReach(self, s, minJump, maxJump):
        q=[0]
        far=1
        for i in q:
            for j in range(max(i+minJump,far),min(i+maxJump+1,len(s))):
                if s[j]=='0':
                    if j==len(s)-1:return True
                    q.append(j)
            far=i+maxJump+1
        return len(s)==1