class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = {}

        for i in edges:
            adj.setdefault(i[0],{})[i[1]] = True
            adj.setdefault(i[1],{})[i[0]] = True
        
        nln = adj.keys()
        while len(adj.keys()) > 2:
            ln = []

            for i in nln:
                if len(adj[i].keys()) == 1:
                    ln.append(i)
            nln = set()
            for i in ln:
                k = list(adj[i].keys()).pop()
                nln.add(k)
                del adj[i]
                del adj[k][i]
        
        return list(adj.keys())

        

            
