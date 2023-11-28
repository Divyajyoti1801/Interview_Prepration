"""
BUY AND SELL STOCKS

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""


def buy_and_sell_stocks(prices):
    l, r = 0, 1  # left_pointer = Buy and right_pointer = sell
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    return max_profit


print("The Maximum Profit we can get : ",
      buy_and_sell_stocks([7, 1, 5, 3, 6, 4]))
