class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 1e9 + 7
        size = 0
        freq = [0] * 26
        result = 0
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        for _ in range(t):
            current = [0] * 26
            current[0] = freq[25]
            current[1] = freq[25]

            for i in range(25):
                current[i + 1] += freq[i] % MOD
            freq = current
        
        result = 0
        for i in range(26):
            result += freq[i] % MOD

        return int(result % MOD)