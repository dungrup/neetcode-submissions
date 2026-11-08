class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = deque()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q.append((r, c))
            visited.add((r,c))
            
            while q:
                r_i, c_i = q.popleft()
                for dr, dc in directions:
                    nr , nc = r_i + dr, c_i + dc
                    if ((nr, nc) not in visited and 
                        0 <= nr < rows and 0 <= nc < columns and
                        grid[nr][nc] == '1'):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1

        
        return islands