class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLUMNS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col)) 

        distance = 0
        while q:
            for idx in range(len(q)):
                r, c = q.popleft()
                visited.add((r,c))
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                grid[r][c] = distance

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLUMNS and
                        (nr, nc) not in visited and grid[nr][nc] != -1):
                        q.append((nr, nc))
                        visited.add((nr, nc))

            distance += 1





        