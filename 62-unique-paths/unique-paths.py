class Solution:
    def factorial(self, num: int) -> int:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    def uniquePaths(self, m: int, n: int) -> int:
        return self.factorial(m + n - 2) // (self.factorial(m - 1) * self.factorial(n - 1))