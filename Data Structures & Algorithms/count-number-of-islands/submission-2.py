class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COULMNS = len(grid), len(grid[0])
        visited = set()
        result = 0

        def bfs(r,c):
            q = deque()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            visited.add((r,c))
            q.append((r,c))

            while q:
                r_i, c_i = q.popleft()
                for d_r, d_c in directions:
                    n_r, n_c = r_i + d_r, c_i + d_c
                    if (0 <= n_r < ROWS  and 0 <= n_c < COULMNS and
                        grid[n_r][n_c] == '1' and (n_r, n_c) not in visited):
                        q.append((n_r, n_c))
                        visited.add((n_r,n_c))

        for row in range(ROWS):
            for col in range(COULMNS):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    result += 1

        return result 
