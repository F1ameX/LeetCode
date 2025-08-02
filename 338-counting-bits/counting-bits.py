class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        for num in range(1, n + 1):
            result.append(result[num >> 1] + num % 2)
        return result