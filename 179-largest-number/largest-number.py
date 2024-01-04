class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        
        def order(x, y):
            ans = 0

            for i, j in zip(x, y):
                if i > j:
                    ans = 1
                    break
                elif i < j:
                    ans = -1
                    break

            if ans != 0:
                return ans
            if len(x) == len(y):
                return 0

            elif len(x) > len(y):
                return order(x[len(y):], y)
            elif len(y) > len(x):
                return order(x, y[len(x):])
            
        for i in range(len(nums), -1, -1):
            for j in range(1, i):
                if order(nums[j-1], nums[j]) < 0:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        return str(int(''.join(nums)))
        