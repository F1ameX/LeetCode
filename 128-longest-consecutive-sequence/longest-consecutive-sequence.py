class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        
        for num in nums:
            counter = 1
            if num - 1 not in nums:
                while num + counter in nums:
                    counter += 1
                result = max(result, counter)
        
        return result