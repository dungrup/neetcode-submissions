class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLUMNS = len(board), len(board[0])

        def dfs(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or
                board[r][c] != 'O'):
                return
            
            board[r][c] = 'T'
            
            dfs(r+1, c)
            dfs(r -1 , c)
            dfs(r , c + 1)
            dfs(r, c - 1)
        
        ## From edge cells mark cells as "T" (unsurrounded temp)
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLUMNS - 1)

        for col in range(COLUMNS):
            dfs(0, col)
            dfs(ROWS - 1, col)

        ## Mark the untouched "O" to "X" since they are surrounded
        for row in range(ROWS):
            for col in range(COLUMNS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'

        ## Now relabel the "T" to "O" since they are not surrounded
        for row in range(ROWS):
            for col in range(COLUMNS):
                if board[row][col] == 'T':
                    board[row][col] = 'O'

        