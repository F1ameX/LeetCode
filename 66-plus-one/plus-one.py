class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        digits = digits[::-1]
        

        for i in range(len(digits)):
            current = digits[i] + carry
            digits[i] = current % 10
            carry = current // 10

        if carry:
            digits.append(carry)
        
        return digits[::-1]
