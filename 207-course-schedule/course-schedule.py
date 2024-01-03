class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
        
        disc = {}
        processed = {}
        ans = True

        def dfs(n):
            nonlocal ans

            if not ans:
                return ans
    
            disc[n] = True

            for v in adj[n]:
                if v in disc and v not in processed:
                    ans = False
                    return ans
                if v not in processed:
                    dfs(v)
            
            processed[n] = True

            return ans
        
        for i in range(numCourses):
            if i not in processed:
                dfs(i)
            
            if not ans:
                return ans
        return ans

        