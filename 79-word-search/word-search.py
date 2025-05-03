class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]

        def backtrack(i: int, j: int, index: int) -> bool:
            if index == len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if visited[i][j] or board[i][j] != word[index]:
                return False

            visited[i][j] = True
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                if backtrack(i + dx, j + dy, index + 1):
                    return True
            visited[i][j] = False
            return False

        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0):
                    return True
        return False