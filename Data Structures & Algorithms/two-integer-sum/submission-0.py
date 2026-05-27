class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for idx in range(len(nums)):
            tgt = target - nums[idx]

            if tgt in my_dict.keys():
                return [my_dict[tgt], idx]
            else:
                my_dict[nums[idx]] = idx

        
