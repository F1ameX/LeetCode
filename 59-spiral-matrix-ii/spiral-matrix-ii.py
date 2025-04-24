class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom = 0, n
        left, right = 0, n
        current = 1
        result = [[0 for _ in range(n)] for _ in range(n)]

        while top < bottom and left < right:
            for i in range(left, right):
                result[top][i] = current
                current += 1
            top += 1

            for i in range(top, bottom):
                result[i][right - 1] = current
                current += 1
            right -= 1

            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    result[bottom - 1][i] = current
                    current += 1
                bottom -= 1

            if left < right:
                for i in range(bottom - 1, top - 1, -1):
                    result[i][left] = current
                    current += 1
                left += 1

        return result
            