class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for left, right in queries:
            diff[left] -= 1
            if right + 1 < n:
                diff[right + 1] += 1
        summa = 0
        for i in range(n):
            summa += diff[i]
            if nums[i] > -summa:
                return False
        return True