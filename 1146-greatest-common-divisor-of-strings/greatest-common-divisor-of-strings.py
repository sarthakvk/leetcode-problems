class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def matchpat(s, pat):
            if len(s) % len(pat) != 0:
                return False
            
            for i in range(len(s)):
                if s[i] != pat[i%len(pat)]:
                    return False
            return True
        ans = ""
        for i in range(min(len(str1), len(str2))):
            if str1[:i+1] != str2[:i+1] or not matchpat(str1, str1[:i+1]) or not matchpat(str2, str1[:i+1]):
                continue
            ans = str1[:i+1]
        return ans

        