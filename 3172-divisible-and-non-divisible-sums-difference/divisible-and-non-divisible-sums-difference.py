class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        array = list(range(1, n + 1))
        num_1 = sum(x for x in array if x % m != 0)
        num_2 = sum(x for x in array if x % m == 0)
        return num_1 - num_2