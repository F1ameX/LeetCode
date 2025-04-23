class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {"(" : 1, ")" : 2, "{" : 3, "}" : 4, "[" : 5, "]" : 6}

        for bracket in s:
            if bracket in ')}]' and len(stack) != 0:
                if dictionary[stack.pop()] - dictionary[bracket] != -1:
                    return False
            else:
                stack.append(bracket)

        return len(stack) == 0