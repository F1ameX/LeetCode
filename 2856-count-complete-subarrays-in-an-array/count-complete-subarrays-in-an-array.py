from collections import defaultdict
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))
        freq = defaultdict(int)
        result = 0
        left = 0
        
        for right in range(len(nums)):
            freq[nums[right]] += 1
            
            while len(freq) == total_unique:
                result+= len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        
        return result