class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        
        for index, letter in enumerate(s, 1):
            if letter == ')':
                if index > 1 and s[index - 2] == '(':
                    dp[index] = dp[index - 2] + 2
                else:
                    current = index - dp[index - 1] - 1
                    if current > 0 and s[current - 1] == "(":
                        dp[index] = dp[index - 1] + 2 + dp[current - 1]
        
        return max(dp)