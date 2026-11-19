class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLUMNS = len(grid), len(grid[0])
        visited = set()
        result = 0

        def bfs(r,c):
            visited.add((r,c))
            q = deque()
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
            q.append((r,c))

            while q:
                ri, ci = q.popleft()
                for dr, dc in directions:
                    nr, nc = ri + dr, ci + dc
                    if ( 0 <= nr < ROWS and 0 <= nc < COLUMNS and
                        grid[nr][nc] == "1" and (nr,nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc)) 



        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col] == '1' and (row,col) not in visited:
                    bfs(row,col)
                    result += 1

        return result
