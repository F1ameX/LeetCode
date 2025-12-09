class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or strs == None:
            return ''

        for i in range(len(strs[0])):
            prefix = strs[0][i]
            for word in strs:
                if i == len(word) or word[i] != prefix:
                    return strs[0][0 : i]
        return strs[0]
        