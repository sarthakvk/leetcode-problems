class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        s = list(s)
        j = len(s) - 1
        l = len(s)
        v = ['a', 'e', 'i', 'o', 'u']
        while i < j:
            if s[i].lower() in v and s[j].lower() in v:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
                continue
            if s[i].lower() not in v:
                i += 1
            if s[j].lower() not in v:
                j -= 1
        
        return "".join(s)

        