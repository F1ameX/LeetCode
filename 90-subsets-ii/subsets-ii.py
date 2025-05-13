class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(start: int, path: List[int]):
            result.append(path.copy())
            for i in range(start, len(nums)):
                if nums[i] == nums[i - 1] and i > start:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return result