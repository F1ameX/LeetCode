class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        needmap = {}

        for num in sorted(nums):
            if hashmap.get(num, 0) == 0:
                continue

            if needmap.get(num, 0) > 0:
                needmap[num] -= 1
                needmap[num + 1] = needmap.get(num + 1, 0) + 1
                hashmap[num] -= 1
            else:
                if hashmap.get(num + 1, 0) > 0 and hashmap.get(num + 2, 0) > 0:
                    hashmap[num] -= 1
                    hashmap[num + 1] -= 1
                    hashmap[num + 2] -= 1
                    needmap[num + 3] = needmap.get(num + 3, 0) + 1
                else:
                    return False

        return True