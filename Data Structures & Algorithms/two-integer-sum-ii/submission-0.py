class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}

        for idx in range(len(numbers)):
            t = target - numbers[idx]
            if t in my_dict:
                return [my_dict[t], idx + 1]
            else:
                my_dict[numbers[idx]] = idx + 1

        

            