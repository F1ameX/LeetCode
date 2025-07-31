class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        index = result = 0

        while index < len(nums):
            counter = 0
            while index < len(nums) and nums[index] == 0:
                counter += 1
                index += 1 
                result += counter
            index += 1
        
        return result
            
