class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(idx: int, combination : List[int]) -> None:
            if len(combination) == k:
                result.append(combination.copy())
                return
            
            for i in range(idx, n + 1):
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()
        
        backtrack(1, [])
        return result