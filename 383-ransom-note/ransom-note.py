class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}

        for char in magazine:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        for char in ransomNote:
            if char in hashmap and hashmap[char] > 0:
                hashmap[char] -= 1
            else:
                return False

        return True