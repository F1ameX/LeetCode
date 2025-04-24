class Solution:
    def factorial(self, n: int) -> int:
        result = 1
        for num in range(1, n + 1):
            result *= num
        return result
    
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(map(str, range(1, n + 1)))
        k -= 1
        result = []

        for i in range(n, 0, -1):
            fact = self.factorial(i - 1)
            index = k // fact
            result.append(nums.pop(index))
            k %= fact
        
        return ''.join(result)