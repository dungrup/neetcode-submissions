class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l , r = 0 , 0
        my_set = set()

        while r < len(s):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1

            my_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len

        

        


