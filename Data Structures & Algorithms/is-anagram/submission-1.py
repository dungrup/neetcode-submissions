class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_list_1 = [0] * 26
        freq_list_2 = [0] * 26

        if len(s) != len(t):
            return False

        for idx in range(len(s)):
            freq_list_1[ord(s[idx]) - ord('a')] += 1
            freq_list_2[ord(t[idx]) - ord('a')] += 1

        if freq_list_1 != freq_list_2:
            return False

        return True

        
        