class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        result = max_k

        while min_k <= max_k:
            mid = (min_k + max_k) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)

            if total_time <= h:
                result = min(result, mid)
                max_k = mid - 1
            else:
                min_k = mid + 1

        return result
            
