class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        ans = 0
        zl = 1
        while j < len(nums):
            if nums[j] == 0:
                if zl > 0:
                    j += 1
                    zl -= 1
                else:
                    while i<=j and nums[i] != 0:
                        i += 1
                    i += 1
                    j += 1
            else:
                j += 1

            ans = max(ans, j-i-1)
        return ans
        