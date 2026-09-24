class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(list)
        output = []

        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1

        freq_list = [[] for _ in range(len(nums) + 1)]

        for key, value in my_dict.items():
            freq_list[value].append(key)

        for idx in range(len(nums), -1, -1):
            if len(output) == k:
                return output
            else:
                for val in freq_list[idx]:
                    output.append(val)
                    
                
        
        return output
                

