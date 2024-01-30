class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = {}

        def bfs(start):
            lvl = [[start]]

            while lvl[-1]:
                nxt = []
                for n in lvl[-1]:
                    for neigh, conn in enumerate(isConnected[n]):
                        if conn and neigh not in visited:
                            nxt.append(neigh)
                            visited[neigh] = True
                lvl.append(nxt)
        ans = 0
        for i in range(len(isConnected)):
            if i not in visited:
                bfs(i)
                ans += 1
        
        return ans