class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene not in bank:
            bank.append(startGene)

        def isom(g1, g2):
            count = 0
            for i, j in zip(g1, g2):
                if i != j:
                    count += 1
            
            return count == 1
        
        lvl = [[startGene]]
        visited = {}

        while lvl[-1]:
            nodes = lvl[-1]
            q = []
            for node in nodes:
                for g in bank:
                    if g not in visited and isom(node, g):
                        if g == endGene:
                            return len(lvl)
                        q.append(g)
                visited[node] = True
            lvl.append(q)
        return -1
            
        