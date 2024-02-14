class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        r, c, d1, d2 = set(), set(), set(), set()

        board = [['.']*n for i in range(n)]
        ans = []
        
        def set_queen(i, j):
            r.add(i)
            c.add(j)
            d1.add(i+j)
            d2.add(i-j)
            board[i][j] = 'Q'

        def rm_queen(i, j):
            r.remove(i)
            c.remove(j)
            d1.remove(i+j)
            d2.remove(i-j)
            board[i][j] = '.'

        def valid_position(i, j):
            return not (i in r or j in c or (i+j) in d1 or (i-j) in d2)

        def solve(n, q=0):
            if q == n:
                ans.append([''.join(i) for i in board])
                return

            for j in range(n):
                if not valid_position(q, j):
                    continue
                set_queen(q, j)
                solved = solve(n, q+1)
                rm_queen(q, j)
        solve(n)
        return ans
        