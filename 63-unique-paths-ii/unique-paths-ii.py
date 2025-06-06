class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[n - 1] = 1

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j + 1 < n:
                    dp[j] = dp[j] + dp[j + 1]

        return dp[0]