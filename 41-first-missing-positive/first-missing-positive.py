from math import isinf

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = float('inf')

        for i in range(len(nums)):
            if not isinf(nums[i]) and abs(nums[i]) <= n:
                nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])

        for i, v in enumerate(nums):
            if v > 0:
                return i + 1
        
        return len(nums) + 1