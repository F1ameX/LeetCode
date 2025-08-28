class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hashmap = defaultdict(list)
        for i, l in enumerate(s):
            hashmap[l].append(i)
        
        result = 0
        for word in words:
            prev = -1
            to_add = True
            for c in word:
                if c not in hashmap:
                    to_add = False
                    break
                idx_list = hashmap[c]
                pos = bisect.bisect_right(idx_list, prev)
                if pos == len(idx_list):
                    to_add = False
                    break
                prev = idx_list[pos]
            if to_add:
                result += 1
        return result