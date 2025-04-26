class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        n = len(s)
        
        digit = False
        dot = False
        exp = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                digit = True
            elif char in '+-':
                if i > 0 and s[i-1].lower() != 'e':
                    return False
            elif char == '.':
                if dot or exp:
                    return False
                dot = True
            elif char.lower() == 'e':
                if exp or not digit:
                    return False
                exp = True
                digit = False
            else:
                return False
        
        return digit