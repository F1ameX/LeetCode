class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return 1

        i = len(s) - 1
        result = 0
        
        while s[i] == ' ':
            i -= 1
        
        while s[i] != ' ' and i >= 0:
            i -= 1
            result += 1
        
        return result