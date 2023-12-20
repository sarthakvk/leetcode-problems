class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            l = d.setdefault(nums[i], [])
            l.append(i)

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem == nums[i] and len(d[rem]) > 1:
                return d[rem]
            elif rem in d and rem != nums[i]:
                return [i, d[rem][0]]



        