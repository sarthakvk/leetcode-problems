from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for w in strs:
            k = ''.join(sorted(w))
            l = d.setdefault(k, [])
            l.append(w)
        
        ans = []

        for i in d.values():
            ans.append(i)
        
        return ans
                

                    

        