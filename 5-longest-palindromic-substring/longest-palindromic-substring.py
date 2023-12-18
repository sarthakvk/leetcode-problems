class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        
        for i in range(len(s)):
            l = i - 1
            r = i + 1


            while r < len(s) and s[r] == s[i]:
                r += 1

            while 0 <= l and r < len(s):
                
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            r -= 1
            l += 1
            if len(s[l:r+1]) > len(ans):
                ans = s[l:r+1]
            
            
        return ans
                    

