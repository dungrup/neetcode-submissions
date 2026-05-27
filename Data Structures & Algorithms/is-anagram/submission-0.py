class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = [0]*26
        freq_t = [0]*26

        if len(s) != len(t):
            return False
        
        for idx in range(len(s)):
            freq_s[ord(s[idx]) - ord('a')] += 1
            freq_t[ord(t[idx]) - ord('a')] += 1

        if freq_s != freq_t:
            return False

        return True
        