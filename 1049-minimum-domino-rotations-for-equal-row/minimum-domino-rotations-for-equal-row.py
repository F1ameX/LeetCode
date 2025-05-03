class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        def check(x: int) -> int:
            rotations_top = rotations_bottom = 0

            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1

                elif tops[i] != x:
                    rotations_top += 1

                elif bottoms[i] != x:
                    rotations_bottom += 1
                
            return min(rotations_top, rotations_bottom)

        candidates = [tops[0], bottoms[0]]

        for candidate in candidates:
            rotations = check(candidate)
            if rotations != -1:
                return rotations
        return -1