class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        wm = {}
        mw = {}

        if len(s) != len(t):
            return False
        for i, j in zip(s, t):
            if i in wm and wm[i] != j:
                return False
            elif i not in wm:
                if j in mw:
                    return False
                wm[i] = j
                mw[j] = True
        return True