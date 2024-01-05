class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        i, j, k = 0, None, None
        x = 1

        while x < len(nums):
            if nums[x] > nums[i]:
                if k and nums[x] > nums[k]:
                    return True
                if j is not None and nums[j] < nums[x]:
                    return True
                else:
                    j = x
                    x += 1
            elif j is None:
                i = x
                x += 1
            else:
                i = x
                k = j
                j = None
        return False

        