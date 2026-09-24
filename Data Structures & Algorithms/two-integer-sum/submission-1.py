class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict(int)
        output = []

        for idx in range(len(nums)):
            t = target - nums[idx]
            if t in num_dict:
                output.append(num_dict[t])
                output.append(idx)
            else:
                num_dict[nums[idx]] = idx

        return output

                