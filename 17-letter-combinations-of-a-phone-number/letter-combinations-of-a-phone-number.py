class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        keyboard = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl', 
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        if len(digits) == 1:
            return list(keyboard[digits[0]])
        
        result = []
        
        def backtrack(i, current):
            if len(current) == len(digits):
                result.append(current)
                return
            for symbol in keyboard[digits[i]]:
                backtrack(i + 1, current + symbol)

        if digits:
            backtrack(0, '')
        
        return result

        

        

        