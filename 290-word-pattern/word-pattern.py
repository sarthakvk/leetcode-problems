class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wl = s.split(" ")
        wm = {}
        mw = {}

        if len(pattern) != len(wl):
            return False

        for w, pat in zip(wl, pattern):
            if pat not in wm and w not in mw:
                wm[pat] = w
                mw[w] = pat
            elif wm.get(pat, '') != w or mw.get(w, '') != pat:
                return False
        
        return True
