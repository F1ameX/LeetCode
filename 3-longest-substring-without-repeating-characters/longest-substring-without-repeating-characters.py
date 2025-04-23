class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        substring = ''
        
        for right in range(len(s)):
            while s[right] in substring:
                substring = substring[1:]
                left += 1
            substring += s[right]

            result = max(result, right - left + 1)

        return result

