from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter()

        for i in nums:
            c[i] += 1

        arr = [[] for i in range(len(nums)+1)]
        print(len(arr), arr)
        for num, cnt in c.items():
            arr[cnt].append(num)
        
        ans = []

        for i in arr[::-1]:
            if len(ans) == k:
                break
            for j in i:
                if len(ans) == k:
                    break
                ans.append(j)


        return ans

