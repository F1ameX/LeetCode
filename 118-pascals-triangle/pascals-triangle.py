class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        result.append([1])
        for i in range(numRows - 1):
            row = [1]
            for j in range(i):
                row.append(result[i][j] + result[i][j + 1])
            row.append(1)
            result.append(row)
        return result