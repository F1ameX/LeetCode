from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(part: str) -> bool:
            return len(part) == 1 or (part[0] != '0' and part.isdigit() and int(part) <= 255)

        def backtrack(start: int, path: List[str]):
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return

            for end in range(start + 1, min(start + 4, len(s) + 1)):
                part = s[start:end]
                if is_valid(part):
                    backtrack(end, path + [part])

        res = []
        if 4 <= len(s) <= 12:
            backtrack(0, [])
        return res