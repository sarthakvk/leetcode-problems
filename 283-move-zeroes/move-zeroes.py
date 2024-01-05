class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lz = len(nums) - 1
        i = 0
        while i <= lz:
            if nums[i] == 0:
                for j in range(i, lz):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                lz -= 1
                if nums[i] != 0:
                    i += 1
            else:
                i += 1

        