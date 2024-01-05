class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = 0
        v = ['a', 'e', 'i', 'o', 'u']
        ans = 0
        vc = 0
        for x in range(len(s)):
            if j - i < k:
                j += 1
                if s[x] in v:
                    ans += 1
            else:
                if s[i] in v:
                    ans -= 1
                if s[x] in v:
                    ans += 1
                i += 1
                j += 1
            vc = max(vc, ans)
        
        return vc

