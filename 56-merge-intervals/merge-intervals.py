class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][-1]:
                result[-1][0] = min(result[-1][0], intervals[i][0])
                result[-1][-1] = max(result[-1][-1], intervals[i][-1])
            else:
                result.append(intervals[i])

        return result