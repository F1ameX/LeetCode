import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        min_time = [[float('inf')] * n for _ in range(m)]
        heap = [(0, 0, 0, 0)] 
        min_time[0][0] = 0

        while heap:
            t, i, j, prev_step = heapq.heappop(heap)

            if i == m - 1 and j == n - 1:
                return t

            if t > min_time[i][j]:
                continue

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    wait = max(t, moveTime[ni][nj])
                    next_step = 2 if prev_step == 1 else 1
                    nt = wait + next_step

                    if nt < min_time[ni][nj]:
                        min_time[ni][nj] = nt
                        heapq.heappush(heap, (nt, ni, nj, next_step))

        return -1