class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = -2147483648
        MAX = 2147483647
        result = 0
        was_digit = False
        sign = 1
        for idx, letter in enumerate(s):
            if was_digit and letter not in "0123456789":
                break
            
            if '0' <= letter <= '9':
                result *= 10
                result += int(letter)
                was_digit = True
                
            else:
                if not was_digit and letter in '+-':
                    was_digit = True
                    if letter == '-':
                        sign = -1
                elif not was_digit and letter not in ' 0123456789':
                    return 0
        
        if MIN < result * sign < MAX:
            return result * sign
        else:
            if sign == -1:
                return MIN
            else:
                return MAX