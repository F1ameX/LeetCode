class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, two, current = -1, len(nums), 0

        while current < two:
            if nums[current] == 0:
                zero += 1
                nums[zero], nums[current] = nums[current], nums[zero]
                current += 1
            
            elif nums[current] == 2:
                two -= 1
                nums[two], nums[current] = nums[current], nums[two]
            
            else:
                current += 1
        
        