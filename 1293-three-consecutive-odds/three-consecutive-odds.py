class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        arr = [1 if x % 2 != 0 else 0 for x in arr]

        for i in range(len(arr) - 2):
            if sum(arr[i: i + 3]) == 3:
                return True
        
        return False