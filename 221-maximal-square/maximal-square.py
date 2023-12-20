class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}
        m, n = len(matrix), len(matrix[0])

        def isSq(i, j):
            if i >= m or j >= n:
                return 0
            
            if dp.get((i,j)):
                return dp[(i,j)]
            
            if matrix[i][j] == "0":
                return 0

            if i == m-1 or j == n-1:
                if matrix[i][j] == "1":
                    ans = 1
                else:
                    ans = 0
                dp[(i,j)] = ans
                return ans

            ans = (1 + min(isSq(i, j+1), isSq(i+1, j), isSq(i+1, j+1))**0.5)**2
            ans = int(ans)
            dp[(i,j)] = ans
            return ans
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    ans = max(isSq(i,j), ans)
        
        return ans