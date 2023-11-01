"""
Problem - 10 : CLIMBING STAIRS

Problem Statement : 
    - You are climbing a staircase. It takes n steps to reach the top.
    - Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2  
"""
def climb_stairs_utility(n,memo):
    if n == 0 or n==1:
        return 1
    if n not in memo:
        memo[n] = climb_stairs_utility(n-1,memo)+climb_stairs_utility(n-2,memo) # type: ignore
    return memo[n]
def climb_stairs(n):
    memo = {}
    return climb_stairs_utility(n,memo)

print("Climb Stairs Problem : ",climb_stairs(4))