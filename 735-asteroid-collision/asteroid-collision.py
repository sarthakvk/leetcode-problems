class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                
                while True:
                    
                    if not stack:
                        stack.append(a)
                        break
                    elif stack[-1] < 0:
                        stack.append(a)
                        break
                    elif abs(a) > stack[-1]:
                        stack.pop()
                    elif abs(a) == abs(stack[-1]):
                        stack.pop()
                        break
                    else:
                        break
        return stack
        