class Solution:
    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[high]

        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1
    
    def quick_sort(self, nums: List[int], low: int, high: int) -> None:
        if low < high:
            pivot = self.partition(nums, low, high)
            self.quick_sort(nums, low, pivot - 1)
            self.quick_sort(nums, pivot + 1, high)
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums) - 1)