class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0]*n
        def pmatch(s, i, j):
            n = len(s)
            ans = 0
            while i < n and j < n and s[i] == s[j]:
                ans += 1
                i += 1
                j += 1
            return ans
        
        i = 1

        while i < n:    
            if z[i-1] > 1:
                l = i - 1
                r = l + z[i-1] - 1
                x = l+1

                while x <= r:
                    if z[x-l] + x <= r:
                        z[x] = z[x-l]
                        x += 1
                    else:
                        l = x
                        match = pmatch(s, r-x+1, r+1)
                        z[x] = match + (r-x+1)
                        r += match
                        x += 1
                i = r + 1
            else:
                z[i] = pmatch(s, 0, i)
                i += 1
        return sum(z) + n




            



