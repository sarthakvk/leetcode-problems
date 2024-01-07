class Solution:
    def longestDupSubstring(self, s: str) -> str:
        l = len(s)
        prime = 10**9+7
        places = [pow(26, i, prime) for i in range(l)]

        def get_int(char):
            return ord(char) - ord('a') + 1

        def check(s1, s2, s, length):
            l = 0

            while l < length:
                if s[s1] != s[s2]:
                    return False
                s1 += 1
                s2 += 1
                l += 1
            return True

        def get_dup(length, s):
            if not length:
                return False
            hmap = {}
            i = 0
            j = length-1
            hsh = 0

            for k in range(length):
               hsh = (hsh + (places[length-1-k]*get_int(s[k]))%prime)%prime
            hmap[hsh] = i
            i += 1
            j += 1
            
            while j < l:
                hsh = (((hsh-(places[length-1]*get_int(s[i-1]))%prime)*26)%prime + (get_int(s[j])*places[0])%prime)%prime

                if hsh in hmap:
                    if check(i, hmap[hsh], s, length):
                        return (i, j)
                
                hmap[hsh] = i

                i += 1
                j += 1

            return False
        
        ans = ""

        start = 1
        end = l

        while start <= end:
            m = (start+end) // 2

            res = get_dup(m, s)

            if res:
                if res[1]-res[0]+1 > len(ans):
                    ans = s[res[0]:res[1]+1]
                start = m + 1
            else:
                end = m - 1
        
        return ans

        