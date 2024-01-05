class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps = []

        for n in nums:
            if ps:
                ps.append(n+ps[-1])
            else:
                ps.append(n)
        
        for i in range(len(nums)):
            ls = ps[i] - nums[i]
            rs = ps[-1] - ps[i]

            if ls == rs:
                return i
        
        return -1
        

