from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        dp = [defaultdict(int) for i in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[j] - nums[i]
                dp[i][diff] += 1

                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    ans += dp[j][diff]
        
        return ans
        