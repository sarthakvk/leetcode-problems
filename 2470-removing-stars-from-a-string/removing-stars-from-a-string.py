class Solution:
    def removeStars(self, s: str) -> str:
        i = 0
        stack = []
        while i < len(s):
            if s[i] != "*":
                stack.append(i)
                i += 1
            else:
                if stack:
                    j = stack.pop(-1)
                    s = s[:j] + s[j+1:]
                    s = s[:i-1] + s[i:]
                    i -= 1
                else:
                    s = s[:i] + s[i+1:]


        
        return s
                


        