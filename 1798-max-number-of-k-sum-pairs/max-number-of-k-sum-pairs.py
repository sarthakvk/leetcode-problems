from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        ans = 0

        for n in nums:
            if c[n] > 0:
                c[n] -= 1
                
                if c[k-n] > 0:
                    c[k-n] -= 1
                    ans += 1
        
        return ans
