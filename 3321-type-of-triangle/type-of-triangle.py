class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return 'none'
        
        if all(nums[i] == nums[i + 1] for i in range(2)):
            return 'equilateral'
        elif any(nums[i] == nums[i + 1] for i in range(2)):
            return 'isosceles'
        elif all(nums[i] != nums[i + 1] for i in range(2)):
            return 'scalene'
        
            