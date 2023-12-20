class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wl = s.split(" ")
        wm = {}
        if len(pattern) != len(wl):
            return False
        if len(set(pattern)) != len(set(wl)):
            return False
        for w, pat in zip(wl, pattern):
            if pat not in wm:
                wm[pat] = w
            elif wm[pat] != w:
                return False
        
        return True
