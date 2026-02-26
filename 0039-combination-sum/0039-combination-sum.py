class Solution(object):
    def combinationSum(self, candidates, target):
        self.ans = []                                   
        def traverse(candid, arr,sm):                    
            if sm == target: self.ans.append(arr)    
            if sm >= target: return                     
            for i in range(len(candid)):                
                traverse(candid[i:], arr + [candid[i]], sm+candid[i])   
        traverse(candidates,[], 0)
        return self.ans
        