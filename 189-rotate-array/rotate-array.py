from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums) 
        deq = deque(nums)
        deq.rotate(k)
        nums[:] = list(deq)
            
        