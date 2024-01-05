class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        ans = [[], []]

        for i in nums1:
            if i not in nums2:
                ans[0].append(i)
        
        for i in nums2:
            if i not in nums1:
                ans[1].append(i)
        
        return ans