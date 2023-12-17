class Solution:
    def rob(self, nums: List[int]) -> int:
        sol = {}
        def dp(idx):
            if idx in sol:
                return sol[idx]

            if idx >= len(nums):
                return 0, False

            if idx == len(nums)-1:
                return nums[idx], True
            
            size = len(nums)
            a1, b1 = dp(idx+1)
            a2, b2 = dp(idx+2)
            na = False
            if a1 > a2+nums[idx]:
                ans = a1
                if not b1:
                    ans += nums[idx]
                    na = True
            else:
                ans = a2 + nums[idx]
                na = True
            
            sol[idx] = (ans, na)
            
            return ans, na

        ans, _ = dp(0)
        return ans
        
