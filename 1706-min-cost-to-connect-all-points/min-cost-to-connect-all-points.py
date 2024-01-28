class Set:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.sub_size = [1]*size
        self.size = size
    
    def find(self, n):
        while n != self.parent[n]:
            n = self.parent[n]
        
        return n
    
    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)

        if self.sub_size[r2] > self.sub_size[r1]:
            r1, r2 = r2, r1
        
        self.parent[r2] = r1
        self.sub_size[r1] += r2
    
    def same(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)
        return r1 == r2


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def get_distance(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])

        ans = 0
        distance = []

        for i in range(len(points)):
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                dist = get_distance(p1, p2)
                distance.append([dist, i, j])
        
        distance.sort(key= lambda x: x[0])
        s = Set(len(points))

        for edge in distance:
            if s.same(edge[1], edge[2]):
                continue
            
            s.union(edge[1], edge[2])
            ans += edge[0]
        
        return ans
