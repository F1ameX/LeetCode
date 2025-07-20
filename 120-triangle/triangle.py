class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[-1]

        for row in range(len(triangle) -1, 0, -1):
            new = []

            for i in range(row):
                new.append(min(triangle[row - 1][i] + prev[i], triangle[row - 1][i] + prev[i + 1]))
                
            prev = new  

        return prev[0] 