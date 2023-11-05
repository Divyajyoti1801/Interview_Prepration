"""
Problem - 12 : BUY AND SELL STOCK

Problem Statement
    - You are given an array prices where prices[i] is the price of a given stock on the ith day.
    - You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.- Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
"""

def buy_and_sell_stock(prices = []):
    max_prices = 0
    left = 0
    right =1
    while right < len(prices):
        current_profit = prices[right] - prices[left]
        if prices[right] > prices[left]:
            max_prices = max(max_prices,current_profit)
        else:
            left = right
        right += 1
    return max_prices

print("Buy and Sell Stock: ",buy_and_sell_stock([7,1,5,3,6,4]))