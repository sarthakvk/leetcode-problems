class Solution:
    def removeStars(self, s: str) -> str:
        i = 0
        stack = []
        ig = set()
        while i < len(s):
            if s[i] != "*":
                stack.append(i)
                i += 1
            else:
                if stack:
                    j = stack.pop(-1)
                    ig.add(j)
                ig.add(i)

                i += 1
        ans = ""

        for i in range(len(s)):
            if i not in ig:
                ans += s[i]
        
        return ans
                


        