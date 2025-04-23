class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = len(nums) - 2

        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1
        
        if left >= 0:
            right = len(nums) - 1
            while right >= 0 and nums[right] <= nums[left]:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        
        nums[left + 1 :] = reversed(nums[left + 1 :])

        return nums
