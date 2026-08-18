class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        maxLen = 0

        for num in my_set:
            if num - 1 not in my_set:
                i_len = 1
                while num + i_len in my_set:
                    i_len +=1

                maxLen = max(maxLen, i_len) 

        return maxLen

        