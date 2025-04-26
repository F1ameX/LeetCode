class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        result = 0
        min_pos = max_pos = bad_pos = -1

        for i in range(n):
            if not (minK <= nums[i] <= maxK):
                bad_pos = i

            if nums[i] == minK:
                min_pos = i
            if nums[i] == maxK:
                max_pos = i

            valid_start = min(min_pos, max_pos)
            if valid_start > bad_pos:
                result += valid_start - bad_pos

        return result