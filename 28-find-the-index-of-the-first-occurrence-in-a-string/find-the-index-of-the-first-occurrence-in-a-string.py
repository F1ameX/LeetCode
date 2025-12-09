class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return -1
        
        n = len(needle)


        for idx in range(len(haystack) + 1 - n):
            if haystack[idx : idx + n] == needle:
                return idx
        
        return -1