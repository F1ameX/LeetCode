class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        result = '/'
        for sym in path.split('/'):
            if sym == '' or sym == '.':
                continue

            elif sym == '..':
                if len(stack) > 0:
                    stack.pop()
                continue

            stack.append(sym)
        

        if len(stack) == 0:
            return '/'
            
        if len(stack) == 1:
            return '/' + stack[0]

        for sym in stack:
            result += sym + '/'
        
        return result[:-1]
        