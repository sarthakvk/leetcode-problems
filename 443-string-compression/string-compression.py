class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        l = len(chars)
        ans = []
        while i < l:
            j = i + 1
            while j < l and chars[j] == chars[i]:
                j += 1
            ans.append(chars[i])
            if j - i > 1:
                ans.extend(list(str(j-i)))
            
            i = j
        for i in range(len(ans)):
            chars[i] = ans[i]
            
        return len(ans)

        