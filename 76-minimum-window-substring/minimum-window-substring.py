from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        wc = Counter(t)
        ans = ""
        left = None
        twc = Counter()
        lr = len(t)

        for j in range(len(s)):
            ch = s[j]
            twc[ch] += 1

            if ch in wc:
                if left is None:
                    left = j
                resize = False
                if j != left and ch == s[left]:
                    while twc[s[left]] > wc[s[left]]:
                        resize = True
                        lw = s[left]
                        twc[lw] -= 1
                        left += 1
                
                if not resize and twc[ch] <= wc[ch]:
                    lr -= 1

                if lr == 0:
                    if not ans or len(ans) > j-left+1:
                        ans = s[left:j+1]
                    
                    twc[s[left]] -= 1
                    lr += 1
                    for i in range(left+1, j+1):
                        if s[i] in wc and twc[s[i]] <= wc[s[i]]:
                            left = i
                            break
                        twc[s[i]] -= 1

        return ans                    