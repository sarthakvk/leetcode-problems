class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        def decode(w, num):
            return w*num
        
        i = 0

        while i < len(s):
            if s[i] != "]":
                stack.append(s[i])
            elif s[i] == "]":
                w = ""
                while stack[-1] != "[":
                    w += stack.pop(-1)[::-1]
                stack.pop()
                
                num = ""
                
                while stack and stack[-1].isnumeric():
                    num += stack.pop()
                num = int(num[::-1])
                stack.append(decode(w[::-1], num))
            i += 1
        
        return "".join(stack)
                


