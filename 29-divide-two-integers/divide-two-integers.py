import sys

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0:
            sign = 1 
        else:
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            div = divisor
            mul = 1
            while dividend >= (div << 1):
                div <<= 1
                mul <<= 1

            dividend -= div
            result += mul

        result *= sign
        
        if result <= -2 ** 31:
            return -2 ** 31
        elif result >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        return result
