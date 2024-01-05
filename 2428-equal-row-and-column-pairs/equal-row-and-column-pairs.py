class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rc = {}
        cc = {}
        ans = 0
        for i in range(n):
            l = rc.setdefault(grid[i][0], [])
            l.append(i)    
            l = cc.setdefault(grid[0][i], [])
            l.append(i)

        for start, idxes in rc.items():
            cols = cc.get(start, [])
            for r in idxes:
                for c in cols:
                    found = True
                    for i in range(n):
                        if grid[i][c] != grid[r][i]:
                            found = False
                            break
                    if cols and found:
                        ans += 1
        
        return ans

        
        