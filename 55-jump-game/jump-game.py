class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0 
        for idx, jump in enumerate(nums):
            if idx > reachable:
                return False
            reachable = max(reachable, idx + nums[idx])
        return True