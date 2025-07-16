class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        current = 1
        for i in range(1, rowIndex + 1):
            value = current * (rowIndex - i + 1) // i
            result.append(value)
            current = value
        return result 