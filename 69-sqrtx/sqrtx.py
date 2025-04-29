class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        result = x
        while result * result > x:
            result = (result + x // result) // 2
        
        return result