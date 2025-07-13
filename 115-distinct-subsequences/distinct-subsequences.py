class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[-1 for _ in range(m)]for _ in range(n)]

        def dfs(i : int, j : int) -> dict[dict[int]]:
            if j < 0:
                return 1 
            elif i < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == t[j]:
                dp[i][j] = dfs(i - 1, j - 1) + dfs(i - 1, j)
            else:
                dp[i][j] = dfs(i - 1, j)

            return dp[i][j]
        
        return dfs(n - 1, m - 1)