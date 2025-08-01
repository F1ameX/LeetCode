class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        for bit in range(32):
            result += (n >> bit) & 1
        
        return result
