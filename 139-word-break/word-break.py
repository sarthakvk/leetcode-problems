class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = {}
        sol = {}
        for w in wordDict:
            t = d.setdefault(w[0],set())
            t.add(w)
        
        def fd(word):
            ans = False
            if not word:
                return True

            if word in sol:
                return sol[word]

            for w in d.get(word[0], set()):
                if len(w) <= len(word):
                    match = True
                    for i in range(len(w)):
                        if w[i] != word[i]:
                            match = False
                    if match:
                        ans = fd(word[len(w):])
                
                if ans:
                    sol[word] = ans
                    return ans
            sol[word] = ans
            return ans
        return fd(s)
            
                    
                    

        