class Solution:
    def isScramble(self, s: str, t: str) -> bool:
        @cache
        def dfs(s1, s2):
            if s1 == s2:
                return True
            if Counter(s1) != Counter(s2):
                return False
            
            N = len(s1)
            for k in range(1, N):
                if (dfs(s1[:k], s2[:k]) and dfs(s1[k:], s2[k:]) or
                    dfs(s1[:k], s2[N - k:]) and dfs(s1[k:], s2[:N - k])):
                    return True
            return False       
        return dfs(s,t)