class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index: int):
            if index == len(nums):
                result.append(current[:])
                return
          
            backtrack(index + 1)
            current.append(nums[index])
            backtrack(index + 1)
            current.pop()

        result = []
        current = []
        backtrack(0)
        return result