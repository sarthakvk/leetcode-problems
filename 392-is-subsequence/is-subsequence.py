class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in s:
            found = False
            for j in range(i, len(t)):
                if t[j] == c:
                    i = j+1
                    found = True
                    break
            if not found:
                return False
        
        return True
            


        