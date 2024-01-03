from queue import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = {}

        for eq, val in  zip(equations, values):
            gn = g.setdefault(eq[0], {eq[0]: float(1)})
            gn[eq[1]] = val

            gn = g.setdefault(eq[1], {})
            gn[eq[0]] = 1/val
        
        def bfs(start, end):
            if start == end and start in g:
                return 1
            elif start not in g or end not in g:
                return -1

            q = deque()
            ans = -1.0
            prnt = {}

            q.append(start)
            found = False
            visited = {}

            while q:
                n = q.popleft()

                if n in visited:
                    continue
                visited[n] = True
                for v in g.get(n, {}).keys():
                    if v in visited:
                        continue
                    prnt[v] = n
                    if v == end:
                        found = True
                        break
                    q.append(v)
                
                if found:
                    t = end
                    ans = 1
                    while t != start:
                        ans *= g[prnt[t]][t]
                        t = prnt[t]
                    break
            return ans
        out = [bfs(i, j) for i, j in queries]
        return out








        