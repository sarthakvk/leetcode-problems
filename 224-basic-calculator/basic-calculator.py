class Solution:
    def calculate(self, s: str) -> int:
        arr = []
        dm = ['+', '-']

        w = ''

        for i in s:
            if i.isnumeric():
                w += i
            else:
                if w:
                    arr.append(w)
                if i and i != ' ':
                    arr.append(i)
                w = ''
        if w:
            arr.append(w)


        stack = []
        
        def solve():
            num = 0

            while stack[-1] != '(':
                n1 = stack.pop(-1)
                s = stack.pop(-1)

                if s == '-':
                    num = num - int(n1)
                elif s == '+':
                    num += int(n1)
                else:
                    num += int(n1)
                    stack.append('(')
                    break
            stack.pop(-1)
            stack.append(num)

        for i in arr:
            if i == ' ':
                continue
            elif i == '+':
                stack.append('+')
            elif i == '-':
                stack.append('-')

            elif i == '(':
                stack.append(i)
            elif i == ')':
                solve()
            elif i.isnumeric():
                stack.append(i)
        
        num = 0

        while stack:
            if len(stack) >= 2:
                n = stack.pop(-1)
                s = stack.pop(-1)
                if s == '-':
                    num = num - int(n)
                elif s == '+':
                    num += int(n)
            if len(stack) == 1:
                n = stack.pop(-1)
                num += int(n)
        return num
