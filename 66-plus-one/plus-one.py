class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1

        while i >= 0:
            num = digits[i] + carry
            digits[i] = num % 10
            carry = num // 10
            i -= 1
            if carry == 0:
                return digits
        
        if carry:
            out = [1]
            out.extend(digits)
            digits = out
        
        return digits