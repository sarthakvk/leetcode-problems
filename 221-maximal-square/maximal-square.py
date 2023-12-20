class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}
        m, n = len(matrix), len(matrix[0])

        def isSq(i, j):
            if i >= m or j >= n:
                return 0
            
            if dp.get((i,j)) is None:

                ans = (1 + min(isSq(i, j+1), isSq(i+1, j), isSq(i+1, j+1)))

                if matrix[i][j] == "1":
                    dp[(i,j)] = ans
                else:
                    dp[(i,j)] = 0

            return dp[(i,j)]
        
        ans = 0
        isSq(0,0)
        for i in dp.values():
            ans = max(ans, i)

        return ans*ans