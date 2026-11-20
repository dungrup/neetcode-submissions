class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        fresh, time = 0 , 0
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row,col))

        while q and fresh > 0:
            for fruit in range(len(q)):
                ri, ci = q.popleft()
                for dr, dc in directions:
                    nr, nc = ri + dr, ci + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLUMNS and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            
            time += 1

        return time if fresh == 0 else -1


        