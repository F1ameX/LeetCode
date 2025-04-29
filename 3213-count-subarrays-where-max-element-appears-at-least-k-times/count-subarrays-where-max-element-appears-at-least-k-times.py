class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        counter = 0
        left = 0
        result = 0

        for right in range(len(nums)):
            if nums[right] == max_num:
                counter += 1
            
            while counter == k:
                if nums[left] == max_num:
                    counter -= 1
                left += 1
            result += left
        
        return result
