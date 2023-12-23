import heapq

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        b = len(batteries)
        sub = sum(batteries[:b-n])
        def canRun(target):
            tsum = sub
            for i in range(b-n, b):
                if batteries[i] >= target:
                    return True
                if tsum >= target - batteries[i]:
                    tsum -= (target - batteries[i])
                else:
                    return False
            return True

        if n == len(batteries):
            return min(batteries)
        
        s = 0
        e = 10**14
        tp = sum(batteries)

        while s <= e:
            m = (s+e) // 2
            cr = canRun(m)
            if cr:
                s = m+1
            else:
                e = m - 1
        return e



            