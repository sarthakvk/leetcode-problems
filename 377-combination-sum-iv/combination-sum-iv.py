class Solution:
    def __init__(self):
        self.dp = {}

    def combinationSum4(self, nums: List[int], target: int) -> int:
        ways = 0
        if target in self.dp:
            return self.dp[target]

        for num in nums:
            if num == target:
                ways += 1
            elif num < target:
                ways += self.combinationSum4(nums, target-num)
        self.dp[target] = ways
        return ways