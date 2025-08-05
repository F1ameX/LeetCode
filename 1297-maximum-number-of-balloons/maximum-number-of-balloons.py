class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = { 'b': 0,
                    'a': 0,
                    'l': 0,
                    'o': 0,
                    'n' : 0
                }
        
        for letter in text:
            if letter in hashmap:
                hashmap[letter] += 1
        hashmap['l'] //= 2
        hashmap['o'] //= 2

        return min(hashmap.values())