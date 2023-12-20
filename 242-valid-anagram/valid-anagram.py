from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1 = Counter(s)
        c2 = Counter(t)

        for k, v in c1.items():
            if c2[k] != v:
                return False

        return True
        