class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        s = list(s)
        ss = [None]*len(s)

        def find_ss(idx):
            ans = []
            t = ''
            for i in range(idx, len(s)):
                t += s[i]
                if t in wordDict:
                    ans.append(i)
            
            return ans
        
        for i in range(len(s)):
            ss[i] = find_ss(i)
        

        def dfs(idx):
            ans = []
            if not ss[idx]:
                return []

            for j in ss[idx]:
                if j == len(s) - 1:
                    ans.append(''.join(s[idx:]))
                else:
                    for w in dfs(j+1):
                        sen = ''.join(s[idx:j+1])+ ' ' + w
                        ans.append(sen)
            return ans
        ans = dfs(0)

        return ans