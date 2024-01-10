class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        last_seen = {}

        i = 0
        j = 0

        while j < len(s):
            if s[j] not in last_seen:
                last_seen[s[j]] = j
            else:
                ls = last_seen[s[j]]
                if i <= ls:
                    i = last_seen[s[j]] + 1
                last_seen[s[j]] = j
            
            ans = max(ans, j-i+1)
            j += 1
        
        return ans

        