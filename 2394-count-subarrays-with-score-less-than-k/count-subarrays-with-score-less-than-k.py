class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        summa = 0
        result = 0
        
        for right in range(n):
            summa += nums[right]
            
            while left <= right and summa * (right - left + 1) >= k:
                summa -= nums[left]
                left += 1
                
            result += (right - left + 1)
        
        return result