class Solution:
    def totalNQueens(self, n: int) -> int:
        r, c, d1, d2 = set(), set(), set(), set()

        ans = 0

        def add_queen(i, j):
            r.add(i)
            c.add(j)
            d1.add(i+j)
            d2.add(i-j)
        
        def rm_queen(i, j):
            r.remove(i)
            c.remove(j)
            d1.remove(i+j)
            d2.remove(i-j)
        
        def is_valid(i, j):
            return not (i in r or j in c or (i+j) in d1 or (i-j) in d2)
        
        def solve(n, q=0):
            nonlocal ans
            if n == q:
                ans += 1
                return
            
            for i in range(n):
                if not is_valid(q, i):
                    continue
                
                add_queen(q, i)
                solve(n, q+1)
                rm_queen(q, i)
        
        solve(n)
        return ans
        