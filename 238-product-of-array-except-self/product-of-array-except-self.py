class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        answer = [1] * len(nums)

        prefix[0] = nums[0]
        postfix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
            postfix[-i] = postfix[-(i - 1)] * nums[-i]
        postfix[0] = postfix[1] * nums[0]

        answer[0] = postfix[1]
        answer[-1] = prefix[-2]
        for i in range(1, len(nums) - 1):
            answer[i] = prefix[i - 1] * postfix[i + 1]

        return answer
