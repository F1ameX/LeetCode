class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1  
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if current > target:
                    right -= 1
                else:
                    left += 1
                    
                if abs(current - target) < abs(closest - target):
                    closest = current
        
        return closest


        