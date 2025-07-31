class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = ''

        for letter in s:
            if 97 <= ord(letter) <= 122 or 48 <= ord(letter) <= 57:
                result += letter
                
        return result == result[::-1]