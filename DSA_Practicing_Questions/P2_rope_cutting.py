"""
Problem - 2 : ROD CUTTING PROBLEM

    Problem Statement:
        - Given a rod of length N inches and an array of prices, price[]. price[i] denotes the value of a piece of length i. Determine the maximum value obtainable by cutting up the rod and selling the pieces.
"""
# def rod_cutting(price,n):
#     dp = [0]*(n+1)
#     dp[1] = price[0]
#     for i in range(2,n+1):
#         m = 0
#         for j in range(1,i):
#             m = max(m,dp[j]+dp[i-j])
#         m = max()

# print("Rod Cutting Problem (DP Problem): ",rod_cutting([2,3,5],9))