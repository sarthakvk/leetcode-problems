class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot():
            start = 0
            end = len(nums) - 1
            mid = 0
            while start < end:
                mid = (start+end) // 2
                
                if mid > 0 and nums[mid] < nums[mid-1]:
                    return mid
                if nums[mid] > nums[-1]:
                    start = mid + 1
                else:
                    end = mid - 1
            return end
        
        pivot = find_pivot()

        if target <= nums[-1]:
            start = pivot
            end = len(nums) - 1
        else:
            start = 0
            end = pivot - 1
        
        while start <= end:
            mid = (start + end) // 2


            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1
