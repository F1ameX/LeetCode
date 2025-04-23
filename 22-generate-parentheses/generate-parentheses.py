class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(opened, closed, curstr):
            if opened == 0:
                for _ in range(closed, 0, -1):
                    curstr += ')'
                result.append(curstr)
                return

            if closed == 0:
                result.append(curstr)
                return

            if closed > opened:
                return backtrack(opened - 1, closed, curstr + '('), backtrack(opened, closed - 1, curstr + ')')
            else:
                return backtrack(opened - 1, closed, curstr + '(')

        backtrack(n - 1, n, '(')

        return result