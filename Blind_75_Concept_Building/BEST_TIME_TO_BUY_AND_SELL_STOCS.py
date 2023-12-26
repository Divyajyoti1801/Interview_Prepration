"""
Best Time To Buy And Sell Stocks

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5

"""


def best_time_to_buy_and_sell_stocks(prices=[]):
    l = 0  # Buy
    r = 1  # Sell
    max_profit = 0

    while r < len(prices):
        if prices[r] - prices[l] < 0:
            l = r
            r += 1

        else:
            max_profit = max(max_profit, prices[r]-prices[l])
            r += 1

    return max_profit


print("Best time to buy and sell stock : ",
      best_time_to_buy_and_sell_stocks([7, 6, 4, 3, 1]))
