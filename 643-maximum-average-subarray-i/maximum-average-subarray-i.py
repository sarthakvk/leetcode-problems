class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        i = 0
        j = k
        ans = sum(nums[0:j])/k
        avg = ans
        while j < len(nums):
            avg = avg + (nums[j]-nums[i])/k
            ans = max(ans, avg)
            i += 1
            j += 1


        return ans