from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge case
        if not grid:
            return 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            nonlocal rows
            nonlocal cols
            nonlocal visited
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if ((r in range(rows)) and (c in range(cols)) and (r,c) not in visited) and (grid[r][c] == "1"):
                        q.append((r,c))
                        visited.add((r,c))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if ((i,j) not in visited and grid[i][j] == "1"):
                    bfs(i,j)
                    islands += 1
        return islands
        
