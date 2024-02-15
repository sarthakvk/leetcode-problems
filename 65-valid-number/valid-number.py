class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        def check_e(s):
            t = s.split('e')
            if len(t) == 1:
                return True
            elif len(t) > 2:
                return False
            t[1] = rm_sign(t[1])
            return t[1].isnumeric()
        
        def rm_sign(s):
            if s and s[0] in ['+', '-']:
                s = s[1:]
            return s

        def rm_e(s):
            if 'e' in s:
                s = s[:s.index('e')]
            return s

        def is_decimal(s):
            s = rm_sign(s)

            if not check_e(s):
                return False
            s = rm_e(s)

            if not s.count('.') == 1:
                return False
            
            t = s.split('.')

            ans = (
                (t[0] == '' and t[1].isnumeric()) or
                (t[1] == '' and t[0].isnumeric()) or
                (t[0].isnumeric() and t[1].isnumeric())
            )

            return ans
        
        def is_int(s):
            s = rm_sign(s)
            if not check_e(s):
                return False
            s = rm_e(s)
            return s.isnumeric()
        
        return is_int(s) or is_decimal(s)
        

        