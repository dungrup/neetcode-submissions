class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0
        
        max_len = 0
        l, r = 0, 1
        my_set = set()

        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            my_set.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len

        

        


