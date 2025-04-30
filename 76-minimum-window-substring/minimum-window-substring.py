class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        start, end = 0, m + 1
        hashmap = collections.defaultdict(int)
        
        for char in t:
                hashmap[char] += 1
        
        left = 0
        for right, char in enumerate(s, 1):
            if hashmap[char] > 0:
                n -= 1
            hashmap[char] -= 1

            if n == 0:
                while hashmap[s[left]] < 0:
                    hashmap[s[left]] += 1
                    left += 1

                if right - left < end - start:
                    start, end = left, right
                
                hashmap[s[left]] += 1
                left += 1
                n += 1
        
        if end > m:
            return ''
        
        return s[start : end]