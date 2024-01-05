class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        fl = k
        ans = 0
        while j < len(nums):
            if nums[j] == 1:
                j += 1
            elif fl > 0:
                j += 1
                fl -= 1
            else:
                while nums[i] != 0:
                    i += 1
                i += 1
                j += 1
            ans = max(ans, j-i)
        
        return ans


        