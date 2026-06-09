class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(x, y):
            visited.add((x, y))
            q = deque([(x, y)])
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if  (0 <= nr < n and 
                        0 <= nc < m and 
                        (nr, nc) not in visited and 
                        grid[nr][nc] == '1'
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))
            
        islands = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
                
        return islands