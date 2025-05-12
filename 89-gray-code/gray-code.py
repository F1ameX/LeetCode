class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            for j in reversed(range(len(result))):
                result.append(result[j] | 1 << i)
        
        return result