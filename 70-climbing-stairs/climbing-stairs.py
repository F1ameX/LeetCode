class Solution:
    def climbStairs(self, n: int) -> int:
        fib_1, fib_2 = 0, 1
        for _ in range(n):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
        
        return fib_2