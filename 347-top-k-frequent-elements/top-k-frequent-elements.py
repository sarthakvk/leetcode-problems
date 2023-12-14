from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter()

        for i in nums:
            c[i] += 1

        arr = [[] for i in range(len(nums)+1)]
        for num, cnt in c.items():
            arr[cnt].append(num)
        
        ans = []

        for i in arr[::-1]:
            for j in i:
                ans.append(j)
                if len(ans) == k:
                    return ans
