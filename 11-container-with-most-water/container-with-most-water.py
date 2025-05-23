class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = min(height[right], height[left]) * (right - left)
        
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

            area = max(area, min(height[right], height[left]) * (right - left))
        return area