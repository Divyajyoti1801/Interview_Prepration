"""
Problem - 1 : COIN CHANGE

    Problem statement:
        = Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ].  
        = NOTE: Assume that you have an infinite supply of each type of coin. And you can use any coin as many times as you want.

Using Algorithm : Dynamic Programming 
    Pseudo Code:
        - the dp[] initialized 0 for all usually but 1 for the index 0 the size of dp , amount + 1
        - Iterate through each denomination.
        -   At each iteration, the value at index `j - coin` in the `solutions` array is added to the value at index `j`. This step accumulates the number of combinations for the current amount using the current coin denomination.
        - The solution will be in DP[-1]
"""
def coin_change(coins,sum):
    dp = [0 if i>0 else 1 for i in range(sum+1)]
    for coin in coins:
        for j in range(coin,sum+1):
            dp[j] += dp[j-coin]
    return dp[-1]
print("Coin Change (Dynamic Programming Problem) : ",coin_change([1,2,3],4))