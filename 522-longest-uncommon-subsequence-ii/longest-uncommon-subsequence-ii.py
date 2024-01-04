class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda x: (-len(x), x))

        check = []

        def check_with_prnt(st):
            for s in check:
                string = st
                for i in s:
                    if not string:
                        return False
                    if string[0] == i:
                        string = string[1:]
                if not string:
                    return False
            return True

        for i in range(1, len(strs)):
            if len(strs[i-1]) != len(strs[i]):
                if check_with_prnt(strs[i-1]):
                    return len(strs[i-1])
                else:
                    check.append(strs[i-1])
            elif strs[i-1] != strs[i]:
                if check_with_prnt(strs[i-1]):
                    return len(strs[i-1])
            else:
                check.append(strs[i-1])
        if check_with_prnt(strs[-1]):
            return len(strs[-1])
        return -1
            

            

        