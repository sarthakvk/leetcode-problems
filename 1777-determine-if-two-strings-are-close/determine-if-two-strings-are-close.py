from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        w1 = Counter(word1)
        w2 = Counter(word2)

        for w in w1:
            if w not in w2:
                return False

        c1 = Counter(w1.values())
        c2 = Counter(w2.values())

        for c, t in c1.items():
            if c2[c] != t:
                return False
        
        return True

