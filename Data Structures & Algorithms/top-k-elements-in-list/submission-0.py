class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}

        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for key, value in my_dict.items():
            freq[value].append(key)

        res = []
        for n in range(len(nums), -1, -1):
            if len(res) == k:
                return res
            else:
                for m in freq[n]:
                    res.append(m)
