class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for word in strs:
            c_count = [0]*26
            
            for c in word:
                c_count[ord(c) - ord('a')] += 1
            
            my_dict[tuple(c_count)].append(word)

        return list(my_dict.values()) 

                


