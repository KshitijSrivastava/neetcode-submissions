class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        i = 0
        j = 1

        while j < n:

            if prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i])
            else:
                i= j

            j += 1


        return max_profit

