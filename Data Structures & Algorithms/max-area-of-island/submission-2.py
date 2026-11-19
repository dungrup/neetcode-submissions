class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or
                grid[r][c] == 0 or (r,c) in visited):
                return 0

            visited.add((r,c))

            return (1 + dfs(r + 1, c) + dfs(r - 1, c) +
                    dfs(r, c + 1) + dfs(r, c - 1))


        for row in range(ROWS):
            for col in range(COLUMNS):
                area = dfs(row,col)
                max_area = max(max_area, area)


        return max_area 
