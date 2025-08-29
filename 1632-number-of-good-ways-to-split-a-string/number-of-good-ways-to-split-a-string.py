class Solution:
    def numSplits(self, s: str) -> int:
        hashmap = {}
        left_set = set()

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        result = 0

        for char in s:
            left_set.add(char)
            hashmap[char] -= 1
            if hashmap[char] == 0:
                hashmap.pop(char)
            
            if (len(hashmap.keys())) == len(left_set):
                result += 1
            
        return result