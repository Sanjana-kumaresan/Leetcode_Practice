class Solution(object):
    def canReach(self, arr, start):
        queue = deque([start])
        visited = set()
        while queue:
            pos = queue.popleft()
            visited.add(pos)  
            if arr[pos] == 0:
                return True  
            next = pos + arr[pos]   
            if next<len(arr) and next not in visited:
                queue.append(next)        
            prev = pos - arr[pos]
            if prev>=0 and prev not in visited:
                queue.append(prev)            
        return False