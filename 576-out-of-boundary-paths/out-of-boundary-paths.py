class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = {}
        mod = 10**9 + 7
        def move(i, j, moves=0):
            nonlocal m, n, maxMove

            if moves > maxMove:
                return 0
            elif (i, j, moves) in dp:
                return dp[(i, j, moves)]
            elif i < 0 or j < 0 or i == m or j == n:
                return 1
            else:
                a = (move(i+1, j, moves=moves+1)%mod)
                b = (move(i-1, j, moves=moves+1)%mod)
                c = (move(i, j+1, moves=moves+1)%mod)
                d = (move(i, j-1, moves=moves+1)%mod)
                dp[(i, j, moves)] = (a+b+c+d)%mod
            
            return dp[(i, j, moves)]
        
        return move(startRow, startColumn)