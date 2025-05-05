class Solution:
    def numTilings(self, n: int) -> int:
        if n < 2:
            return 1
        elif n == 2:
            return 2

        dp = [1 for _ in range(n + 1)]
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]

        return dp[n] % (10 ** 9 + 7)