class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        order = [0]*n
        adj = [[0]*n for i in range(n)]
        for i, j in roads:
            order[i] += 1
            order[j] += 1
            adj[i][j] = 1
            adj[j][i] = 1
        
        ans = 0
        
        for i in range(n):
            for j in range(i+1, n):
                mf = order[i] + order[j]

                if adj[i][j]:
                    mf -= 1
                ans = max(ans, mf)
        
        return ans