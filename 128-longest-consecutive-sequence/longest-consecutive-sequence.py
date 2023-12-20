class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        c = {}
        nn = set()
        ans = 0
        x = y = None
        for n in m:
            if n in nn:
                continue
            s = n+1
            a = 1

            while s in m:
                nn.add(s)
                if s in c:
                    a += c[s]
                    break
                a+= 1
                s += 1
            c[n] = a
            
            ans = max(ans, a)
        return ans

        