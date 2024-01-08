class Solution:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        dp = [[0]*(n+1) for _ in range(n+1)] # the dp[i][l] is how many ways if word ends at i with length l

        for i in range(n):
            for l in range(1, i+2):
                j = i - l + 1
                cur = 0

                if num[j] == '0':
                    cur = 0
                elif j == 0:
                    cur = 1
                elif j < l:
                    cur = dp[j-1][j]
                elif num[j-l:j] <= num[j:i+1]:
                    cur = dp[j-1][l]
                else:
                    cur = dp[j-1][l-1]
                
                dp[i][l] = dp[i][l-1] + cur
        
        return dp[n-1][n]%(10**9+7)
                
