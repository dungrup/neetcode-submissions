class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        n = len(nums)

        prefix = 1

        for idx in range(n):
            answer[idx] = prefix
            prefix *= nums[idx]

        suffix = 1

        for idx in range(n - 1, -1, -1):
            answer[idx] *= suffix
            suffix *= nums[idx]

        return answer