from heapq import *

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = []
        ans = 0
        tree = [False]*len(points)
        def get_distance(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        v = 0

        while not tree[v]:
            tree[v] = True

            for i in range(len(points)):
                if tree[i]:
                    continue
                dist = get_distance(points[v], points[i])
                heappush(pq, (dist, v, i))
            
            if not pq:
                break

            nxt_edge = heappop(pq)
            
            while pq and tree[nxt_edge[2]]:
                nxt_edge = heappop(pq)
            if not tree[nxt_edge[2]]:
                ans += nxt_edge[0]
                v = nxt_edge[2]
        
        return ans
