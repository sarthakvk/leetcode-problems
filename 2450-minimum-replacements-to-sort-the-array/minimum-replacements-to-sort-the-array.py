class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        def split_till_sm(n1, n2):
            op = (n1-1)//n2
            return n1//(op+1), op

        ans = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                n, op = split_till_sm(nums[i], nums[i+1])
                # print(f"Split {nums[i]} to {n} by {op}")
                nums[i] = n
                ans += op
        
        return ans
        