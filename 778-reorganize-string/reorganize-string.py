class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        max_heap = [(-frequency, char) for char, frequency in hashmap.items()]
        heapq.heapify(max_heap)

        result = []
        prev_frequency, prev_char = 0, ""

        while max_heap:
            frequency, char = heapq.heappop(max_heap)
            result.append(char)

            if prev_frequency < 0:
                heapq.heappush(max_heap, (prev_frequency, prev_char))

            frequency += 1
            prev_frequency, prev_char = frequency, char
        
        if len(result) != len(s):
            return ""
        
        return "".join(result)