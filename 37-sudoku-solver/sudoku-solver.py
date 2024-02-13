class Solution:
    def in_row(self, row, val, board):
        for i in range(9):
            if board[row][i] == val:
                return True
        
        return False

    def in_col(self, col, val, board):
        for i in range(9):
            if board[i][col] == val:
                return True
        
        return False

    def in_subbox(self, br, bc, val, board):
        r = br*3
        c = bc*3

        for i in range(r,r+3):
            for j in range(c, c+3):
                if board[i][j] == val:
                    return True
        return False

    def solve(self, board: List[List[str]]) -> bool:
        """
        Do not return anything, modify board in-place instead.
        """
        empty = None
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue  
                empty = (i, j)
        
        if not empty:
            return True
        
        i, j = empty
        for n in range(1, 10):
            v = str(n)
            in_sub = self.in_subbox(i//3, j//3, v, board)
            in_row = self.in_row(i, v, board)
            in_col = self.in_col(j, v, board)
            
            if (in_sub or in_row or in_col):
                continue
            
            board[i][j] = v
            if self.solve(board):
                return True
            else:
                board[i][j] = '.'
        
        return False

    def solveSudoku(self, board: List[List[str]], sr=0, sc=0) -> None:
        self.solve(board)
