class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = {}

        for i in edges:
            adj.setdefault(i[0],{})[i[1]] = True
            adj.setdefault(i[1],{})[i[0]] = True
        
        while len(adj.keys()) > 2:
            ln = []
            for i in adj.keys():
                if len(adj[i].keys()) == 1:
                    ln.append(i)
            
            for i in ln:
                k = list(adj[i].keys()).pop()
                del adj[i]
                del adj[k][i]
        
        return list(adj.keys())

        

            
