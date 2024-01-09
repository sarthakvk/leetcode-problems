class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1]))
        ans = 0
        i = 1
        j = 0
        while i < len(intervals):
            if intervals[j][1] > intervals[i][0]:
                ans += 1
                i += 1
            else:
                j = i
                i += 1
        
        return ans
        