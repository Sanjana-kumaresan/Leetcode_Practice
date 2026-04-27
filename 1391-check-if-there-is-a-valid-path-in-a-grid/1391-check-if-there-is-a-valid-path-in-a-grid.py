class Solution(object):
    def hasValidPath(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        dirs = {
            1: [(0,1,{1,3,5}), (0,-1,{1,4,6})],
            2: [(1,0,{2,5,6}), (-1,0,{2,3,4})],
            3: [(0,-1,{1,4,6}), (1,0,{2,5,6})],
            4: [(0,1,{1,3,5}), (1,0,{2,5,6})],
            5: [(0,-1,{1,4,6}), (-1,0,{2,3,4})],
            6: [(0,1,{1,3,5}), (-1,0,{2,3,4})]
        }
        def dfs(i, j):
            if (i, j) == (rows-1, cols-1):
                return True
            visited.add((i, j))
            for dx, dy, valid in dirs[grid[i][j]]:
                ni, nj = i+dx, j+dy
                if (0 <= ni < rows and 0 <= nj < cols and
                    grid[ni][nj] in valid and (ni, nj) not in visited):
                    if dfs(ni, nj):
                        return True
            return False
        return dfs(0, 0)