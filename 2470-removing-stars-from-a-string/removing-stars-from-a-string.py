class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for i in s:
            if i == "*" and stack:
                stack.pop(-1)
            elif i != "*":
                stack.append(i)
        return "".join(stack)
                


        