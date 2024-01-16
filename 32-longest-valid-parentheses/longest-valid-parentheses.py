class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = [0] * len(s)
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif stack:
                ans[stack.pop(-1)] = 1
                ans[i] = 1
        
        i = 0
        j = 0
        out = 0

        while j <= len(s):
            if j < len(s) and ans[j] == 1:
                j += 1
            else:
                out = max(out, j-i)
                j += 1
                i = j
        
        return out

        