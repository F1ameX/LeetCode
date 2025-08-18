class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for anagram in strs:
            current = ''.join(sorted(anagram))
            if current not in hashmap:
                hashmap[current] = [anagram]
            else:
                hashmap[current].append(anagram)
        
        return [hashmap[seq] for seq in hashmap]