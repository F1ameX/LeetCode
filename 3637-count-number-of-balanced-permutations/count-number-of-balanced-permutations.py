class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        digits = list(map(int, num))
        total_sum = sum(digits)
        length = len(digits)

        if total_sum % 2 != 0:
            return 0

        half_sum = total_sum // 2
        left_count = length // 2
        right_count = length - left_count
        freq = Counter(digits)

        @lru_cache(maxsize=None)
        def explore(digit: int, remaining_sum: int, left: int, right: int) -> int:
            if digit > 9:
                return int((remaining_sum | left | right) == 0)

            if left == 0 and remaining_sum != 0:
                return 0

            result = 0
            max_left = min(freq[digit], left)

            for l_used in range(max_left + 1):
                r_used = freq[digit] - l_used
                if 0 <= r_used <= right and l_used * digit <= remaining_sum:
                    ways = comb(left, l_used) * comb(right, r_used)
                    result = (result + ways * explore(digit + 1, remaining_sum - l_used * digit, left - l_used, right - r_used)) % MOD

            return result

        return explore(0, half_sum, left_count, right_count)