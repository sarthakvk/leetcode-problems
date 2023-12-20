class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[None for i in range(n)] for j in range(m)]

        def isSq(i, j):
            if i >= m or j >= n:
                return 0
            
            if dp[i][j] is None:

                ans = (1 + min(isSq(i, j+1), isSq(i+1, j), isSq(i+1, j+1)))

                if matrix[i][j] == "1":
                    dp[i][j] = ans
                else:
                    dp[i][j] = 0

            return dp[i][j]
        
        ans = 0
        isSq(0,0)
        for i in range(m):
            for j in range(n):
                ans = max(ans, dp[i][j])

        return ans*ans