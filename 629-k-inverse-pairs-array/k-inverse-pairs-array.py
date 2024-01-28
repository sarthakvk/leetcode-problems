class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0]*(k+1) for i in range(n+1)]
        dp[0][0] = 1
        mod = 10**9 + 7
        for i in range(1, n+1):
            for j in range(k+1):
                if j > (i*(i-1)//2):
                    break
                if j == 0:
                    dp[i][j] = 1
                else:
                    if i <= j:
                        dp[i][j] = (dp[i][j-1] - dp[i-1][j-i] + dp[i-1][j])%mod
                    else:
                        dp[i][j] = (dp[i][j-1] + dp[i-1][j])%mod
        return dp[n][k]
                    
                
        