"""
Title : Best Time to Buy and Sell Stock
Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        ans = 0
        for x in prices:
            if min_price > x:
                min_price = x
            elif ans < (max_profit := x - min_price):
                ans = max_profit
        return ans


if __name__ == "__main__":
    pass
