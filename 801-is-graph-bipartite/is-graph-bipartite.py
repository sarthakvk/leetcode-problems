class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = set()
        a = set()
        b = set()

        def bfs(start):
            lvl = [[start]]
            a.add(start)
            color.add(start)

            while lvl[-1]:
                nxt = []

                for n in lvl[-1]:
                    for neigh in graph[n]:
                        if neigh in color:
                            if neigh in a and n in a:
                                return False
                            elif neigh in b and n in b:
                                return False
                        else:
                            if n in a:
                                b.add(neigh)
                            else:
                                a.add(neigh)
                            nxt.append(neigh)
                            color.add(neigh)
                lvl.append(nxt)
            return True
        
        for i in range(len(graph)):
            if i not in color:
                if not bfs(i):
                    return False

        return True