class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for word in strs:
            num = [0]*26
            for idx in range(len(word)):
                num[ord(word[idx]) - ord('a')] += 1
            my_dict[tuple(num)].append(word)
            
        return list(my_dict.values())

                


