class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[None for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n3 != n1+n2:
            return False

        def ci(i, j, k):
            if dp[i][j] is not None:
                return dp[i][j]

            a1 = a2 = False
            if i == n1 and j == n2 and k == n3:
                return True

            elif i < n1 and j < n2:
                if s1[i] == s3[k]:
                    a1 = ci(i+1, j, k+1)
                if s2[j] == s3[k]:
                    a2 = ci(i, j+1, k+1)
                
            elif i < n1:
                if s1[i] == s3[k]:
                    a1 = ci(i+1, j, k+1)
            elif j < n2:
                if s2[j] == s3[k]:
                    a2 = ci(i, j+1, k+1)
            
            ans = a1 or a2
            dp[i][j] = ans
            return ans
        
        ans = ci(0,0,0)
        return ans
