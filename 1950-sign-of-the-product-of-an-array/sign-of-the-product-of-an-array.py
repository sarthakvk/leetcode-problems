class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1

        for n in nums:
            if n == 0:
                return 0
            ans *= int(n/abs(n))
        
        return ans
        