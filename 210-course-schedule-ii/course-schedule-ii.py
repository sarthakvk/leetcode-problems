class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        disc = {}
        processed = {}
        cycle = False
        ans = []
        adjs = [[] for i in range(numCourses)]

        for a, b in prerequisites:
            adjs[a].append(b)

        def dfs(adj, node):
            nonlocal cycle
            if cycle:
                return []
            disc[node] = True
            for v in adj[node]:
                if v in disc and v not in processed:
                    cycle = True
                    return []
                if v not in processed:
                    dfs(adj, v)
            processed[node] = True
            ans.append(node)
        
        for i in range(numCourses):
            if i not in processed:
                dfs(adjs, i)
            if cycle:
                return []
        return ans