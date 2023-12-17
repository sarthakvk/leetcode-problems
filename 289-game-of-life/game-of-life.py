class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def getN(i,j):
            neig = {
                (i, j+1),
                (i, j-1),
                (i+1, j),
                (i-1, j),
                (i-1, j-1),
                (i-1, j+1),
                (i+1, j+1),
                (i+1, j-1),
            }
            to_rm = []
            for ne in neig:
                x,y = ne

                if not ((0 <= x <m) and (0 <= y < n)):
                    to_rm.append(ne)
            
            for r in to_rm:
                neig.remove(r)
            
            return neig



        for i in range(m):
            for j in range(n):
                neigh = getN(i, j)
                lc = 0

                for x, y in neigh:
                    print(x,y)
                    if board[x][y] in [-1,1]:
                        lc += 1
                
                if board[i][j] == 1:
                    if lc < 2 or lc >3:
                        board[i][j] = -1
                elif lc == 3:
                    board[i][j] = 2
        

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0
        
        return board



