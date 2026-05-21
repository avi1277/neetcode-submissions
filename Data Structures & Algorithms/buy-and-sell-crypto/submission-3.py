class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lower = prices[0]
        higher = prices[0]
        profit = 0

        for num in prices:

            if num > higher:
                higher = num
            if num < lower:
                lower = num
                higher = 0
        

            if higher - lower > profit:
                profit = higher - lower
                
        return profit