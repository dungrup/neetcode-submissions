class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {} ##{val: count}
        output = []

        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1

        freq_list = [[] for _ in range(len(nums) + 1)]
        
        for val, count in my_dict.items():
            freq_list[count].append(val)

        for idx in range(len(nums), -1 , -1):
            if len(output) == k:
                return output
            
            for vals in freq_list[idx]:
                output.append(vals)
                if len(output) == k:
                    break
                
        return output



