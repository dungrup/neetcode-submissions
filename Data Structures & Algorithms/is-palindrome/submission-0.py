class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.strip().lower()

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not new_s[left].isalnum():
                left += 1
            while left < right and not new_s[right].isalnum():
                right -= 1
            
            if new_s[left] == new_s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True