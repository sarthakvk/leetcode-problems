class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0]*(n+1)

        for i in range(n-1, -1, -1):
            dp[i] = 1 + dp[i+1]

            for w in dictionary:
                if len(w) <= n-i and s[i:i+len(w)] == w:
                    dp[i] = min(dp[i], dp[i+len(w)])
        return dp[0]
        