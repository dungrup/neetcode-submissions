class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        l , r = 0, 1

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            if curr_profit <= 0:
                l = r
            else:
                max_p = max(curr_profit, max_p)
            
            r += 1

        return max_p


