class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-2, -1, -1):
            op = (nums[i]-1)//(nums[i+1])
            ans += op
            nums[i] = nums[i]//(op+1)
        return ans