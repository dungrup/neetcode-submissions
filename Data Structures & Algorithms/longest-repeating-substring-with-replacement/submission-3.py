class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        result = 0
        maxf = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxf = max(maxf, counts[s[r]])
            while r - l + 1 - maxf > k:
                counts[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result
            


