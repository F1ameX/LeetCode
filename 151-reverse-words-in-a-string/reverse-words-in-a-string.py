class Solution:
    def reverseWords(self, s: str) -> str:
        deq = deque()
        i = 0
        n = len(s)

        while i < n:
            if s[i] == ' ':
                i += 1
                continue

            j = i
            while j < n and s[j] != ' ':
                j += 1

            word = s[i:j]
            deq.appendleft(word)

            i = j

        return ' '.join(deq)