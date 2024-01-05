class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zc = 0

        for n in nums:
            if n:
                prod *= n
            else:
                zc += 1

        if zc > 1:
            return [0]*len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = prod
            elif zc == 1:
                nums[i] = 0
            else:
                nums[i] = prod // nums[i]
        
        return nums