class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float('inf')
        out = ans
        for n in nums:
            ans = max(ans+n, n)
            out = max(ans, out)
        
        return out