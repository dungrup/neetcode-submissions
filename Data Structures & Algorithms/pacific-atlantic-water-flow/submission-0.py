class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLUMNS = len(heights), len(heights[0])
        pac , atl = set(), set()

        def dfs(r, c, visited, prevHt):
            if (r >= ROWS or r < 0 or c >= COLUMNS or c < 0 or
                heights[r][c] < prevHt or (r,c) in visited):
                return
            
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
        
        for col in range(COLUMNS):
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])
        
        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLUMNS - 1, atl, heights[row][COLUMNS - 1])

        result = []
        for ri in range(ROWS):
            for ci in range(COLUMNS):
                if (ri, ci) in pac and (ri,ci) in atl:
                    result.append([ri, ci])

        return result
