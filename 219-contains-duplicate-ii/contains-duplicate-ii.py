class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}

        for i in range(len(nums)):
            l = m.setdefault(nums[i], [])
            l.append(i)
        
        for i in m.values():
            i.sort()
            for j in range(1, len(i)):
                if i[j] - i[j-1] <= k:
                    return True
        
        return False
        