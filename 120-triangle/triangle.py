class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        h = len(triangle)
        for i in range(h):
            dp.append([None]*(i+1))
        
        def sol(n,m):
            if dp[n][m] is not None:
                return dp[n][m]

            if n == h-1:
                return triangle[n][m]
            
            ans = min(sol(n+1,m), sol(n+1,m+1)) + triangle[n][m]

            dp[n][m] = ans

            return ans
        
        return sol(0,0)

