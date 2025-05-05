class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if not nums:
            return False

        pivot = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                pivot = i + 1
                break

        if pivot == 0:
            left, right = 0, n - 1
        elif target >= nums[0]:
            left, right = 0, pivot - 1
        else:
            left, right = pivot, n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False