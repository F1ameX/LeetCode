class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = Counter()
        result = 0 

        for num_1, num_2 in dominoes:
            if num_1 < num_2:
                x = num_1 * 10 + num_2
            else:
                x = num_2 * 10 + num_1

            result += counter[x]
            counter[x] += 1
        
        return result