class Solution:
    def getWordsInLongestSubsequence(self, w: List[str], g: List[int]) -> List[str]:
        n = len(w)
        @lru_cache(None)
        def dp(idx: int) -> List[str]:
            best = []
            for j in range(idx + 1, n):
                if g[idx] != g[j] and len(w[idx]) == len(w[j]) and \
                   sum(a != b for a, b in zip(w[idx], w[j])) == 1:
                    candidate = dp(j)
                    if len(candidate) > len(best):
                        best = candidate
            return [w[idx]] + best
        
        return max((dp(i) for i in range(n)), key=len)