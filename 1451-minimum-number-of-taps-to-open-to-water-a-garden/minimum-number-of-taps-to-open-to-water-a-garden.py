class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        ans = 0

        for i in range(n+1):
            intervals.append([i-ranges[i], i+ranges[i]])
        
        intervals.sort(key=lambda x: x[0])
        intervals.append([float('inf'), float('inf')])
        j = 0
        max_end = -float('inf')
        idx = 0
        while idx <= n+1:
            interval = intervals[idx]
            if j >= n:
                break
            if interval[0] <= j <= interval[1]:
                max_end = max(max_end, interval[1])
                idx += 1
            elif j > interval[1]:
                idx += 1
            else:
                if max_end == -float('inf'):
                    return -1
                else:
                    j = max_end
                    max_end = -float('inf')
                    ans += 1
        
        return ans

        