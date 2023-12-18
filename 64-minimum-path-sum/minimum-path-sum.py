class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        e = (len(grid)-1,len(grid[0])-1)
        dp = [[float('inf') for i in range(e[1]+1)] for j in range(e[0]+1)]

        def sol(x, y):
            if x == e[0] and y == e[1]:
                dp[x][y] = grid[x][y]
                return grid[x][y]
            elif x > e[0] or y > e[1]:
                return float('inf')
            elif dp[x][y] != float('inf'):
                return dp[x][y]

            p1 = x+1, y
            p2 = x, y+1

            ans = min(sol(*p1), sol(*p2)) + grid[x][y]
            dp[x][y] = ans
            return ans

        return sol(0,0)



        