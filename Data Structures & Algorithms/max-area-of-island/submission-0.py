from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # edge case
        if not grid:
            return 0
        # initialize our trackers
        visited = set()
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(i, j):
            nonlocal visited
            nonlocal rows, cols
            nonlocal max_area
            q = deque()
            q.append((i,j))
            visited.add((i,j))

            curr_area = 1

            # go through queue
            while q:
                row, col = q.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    # check element valid and add to queue and visited
                    if (r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))

                        # increment current area
                        curr_area += 1
            if max_area < curr_area:
                max_area = curr_area
            


        
        for i in range(rows):
            for j in range(cols):
                # check if element is 1 and not in visited and perform bfs
                if grid[i][j] == 1 and (i,j) not in visited:
                    bfs(i,j)
        return max_area
