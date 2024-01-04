from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)

        ans = 0

        for val in count.values():
            if val % 3 == 0:
                ans += (val // 3)        
            elif val % 3 == 1:
                if val < 3:
                    return -1
                ans += (val-4)//3 + 2
            else:
                ans += (val-2)//3 + 1
        
        return ans