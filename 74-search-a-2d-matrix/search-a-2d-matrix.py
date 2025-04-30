class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        current_row = 0
        for i in range(len(matrix)):
            print(matrix[i])
            if matrix[i][-1] == target:
                return True
            elif matrix[i][-1] > target:
                current_row = i
                break

        left = 0
        right = len(matrix[current_row]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[current_row][mid] == target:
                return True
            
            elif matrix[current_row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False