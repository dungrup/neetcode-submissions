class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        my_set = set(nums)

        for num in nums:
            if num - 1 in my_set:
                continue
            
            op = 0
            while num in my_set:
                op += 1
                num += 1

            max_len = max(max_len, op)

        return max_len

                

        