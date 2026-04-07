from collections import deque
class Solution:
    def cutOffTree(self, f):
        m,n=len(f),len(f[0])
        trees=sorted((f[i][j],i,j) for i in range(m) for j in range(n) if f[i][j]>1)       
        def bfs(sx,sy,tx,ty):
            q=deque([(sx,sy,0)])
            vis={(sx,sy)}
            while q:
                x,y,d=q.popleft()
                if (x,y)==(tx,ty): return d
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and f[nx][ny] and (nx,ny) not in vis:
                        vis.add((nx,ny))
                        q.append((nx,ny,d+1))
            return -1    
        x=y=res=0
        for _,i,j in trees:
            d=bfs(x,y,i,j)
            if d<0: return -1
            res+=d
            x,y=i,j
        return res