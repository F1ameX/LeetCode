class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        append = result.append

        for current in intervals[1:]:
            last = result[-1]
            if current[0] <= last[1]:
                if current[0] < last[0]:
                    last[0] = current[0]
                if current[1] > last[1]:
                    last[1] = current[1]
            else:
                append(current)

        return result