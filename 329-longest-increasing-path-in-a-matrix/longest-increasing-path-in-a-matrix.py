class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[None]*n for i in range(m)]

        def valid(i, j):
            nonlocal m, n
            return not (i < 0 or j < 0 or i >= m or j >= n)
        
        def get_val(i, j):
            if not valid(i, j):
                return -float('inf')
            return matrix[i][j]

        def dfs(i, j, size=1):
            if not valid(i, j):
                return 0
            elif dp[i][j]:
                return dp[i][j]
            else:
                val = matrix[i][j]
                a = dfs(i, j+1) if get_val(i, j+1) > val else 0
                b = dfs(i, j-1) if get_val(i, j-1) > val else 0
                c = dfs(i+1, j) if get_val(i+1, j) > val else 0
                d = dfs(i-1, j) if get_val(i-1, j) > val else 0
                dp[i][j] = max(a,b,c,d) + 1

            return dp[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(dfs(i, j), ans)
        return ans


        