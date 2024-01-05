class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        r = Counter()
        c = Counter()
        ans = 0
        for i in range(n):
            r_val = ''
            c_val = ''
            for j in range(n):
                r_val += str(grid[i][j]) + "-"
                c_val += str(grid[j][i]) + "-"
            
            r[r_val] += 1
            c[c_val] += 1
        for k, v in r.items():
            if k in c:
                ans += (v*c[k])
        
        return ans