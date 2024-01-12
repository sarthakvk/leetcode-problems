from collections import Counter

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vovels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        a1 = 1

        for i in range(len(s)):
            if s[i] in vovels:
                if i < len(s)//2:
                    a1 <<= 1
                else:
                    a1 >>= 1
        
        return a1 == 1

        