class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        n = int(bin(n)[2:])
        while n:
            result += (n & 1) == 1
            n //=10
        
        return result
