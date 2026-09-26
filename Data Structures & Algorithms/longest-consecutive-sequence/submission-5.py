class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        my_set = set(nums)

        for val in my_set:
            if val - 1 in my_set:
                continue
            
            curr_max = 0
            while val in my_set:
                curr_max += 1
                val += 1

            output = max(output, curr_max)

        return output

                

        