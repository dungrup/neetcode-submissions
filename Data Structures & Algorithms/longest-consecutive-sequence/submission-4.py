class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_len = 0

        for num in my_set:
            if num - 1 not in my_set:
                temp_len = 0
                while num in my_set:
                    temp_len += 1
                    max_len = max(max_len, temp_len)
                    num += 1

        return max_len

                

        