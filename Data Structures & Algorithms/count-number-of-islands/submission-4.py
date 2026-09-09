from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # edge case 
        if not grid:
            return 0
        # initialize trackers
        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(i,j):
            nonlocal visited
            nonlocal rows, cols
            q = deque()
            q.append((i,j))
            visited.add((i,j))

            # check adjacent elements
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if ((r in range(rows)) and (c in range(cols)) and (grid[r][c] == "1") and ((r,c) not in visited)):
                        q.append((r,c))
                        visited.add((r,c))

        # matrix traversal
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1

        return islands
