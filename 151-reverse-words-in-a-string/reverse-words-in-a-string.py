class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        ans = []

        for i in s:
            if i:
                ans.append(i)
        
        i = 0
        j = len(ans) - 1

        while i < j:
            ans[i], ans[j] = ans[j], ans[i]
            i += 1
            j -= 1
        
        return " ".join(ans)

            

            


        