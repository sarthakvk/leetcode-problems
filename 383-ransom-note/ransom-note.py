from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)

        for k, v in rc.items():
            if mc[k] < v:
                return False
        
        return True
        