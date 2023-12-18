class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1:
            return 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
                else:
                    obstacleGrid[i][j] = None
        
        obstacleGrid[m-1][n-1] = 1
        
        def sol(x, y):
            if x >= m or y >= n:
                return -1

            if obstacleGrid[x][y] == -1:
                return -1

            elif obstacleGrid[x][y] is not None:
                return obstacleGrid[x][y]
            else:
                ans = max(sol(x+1, y),0) + max(sol(x, y+1), 0)
                obstacleGrid[x][y] = ans
                return ans
        
        return max(sol(0, 0), 0)


        