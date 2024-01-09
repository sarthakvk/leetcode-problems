class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)

        cmp = 1
        start = 1
        for i in range(1, n+1):
            if i < cmp:
                dp[i] = 1 + dp[start]
                start += 1
            else:
                start = 1
                cmp <<= 1
                dp[i] = 1
        
        return dp
        