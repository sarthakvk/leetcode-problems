class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[None for j in range(l2+1)] for i in range(l1+1)]
        
        def dfs(i, j):
            if i == l1:
                ans = l2 - j
            elif j == l2:
                ans = l1 - i
            elif dp[i][j] is not None:
                return dp[i][j]
            elif word1[i] == word2[j]:
                ans = dfs(i+1, j+1)
            else:
                o1 = 1 + dfs(i, j+1)
                o2 = 1 + dfs(i+1, j)
                o3 = 1 + dfs(i+1, j+1)

                ans = min(o1, o2, o3)
            
            dp[i][j] = ans

            return ans
        
        return dfs(0,0)