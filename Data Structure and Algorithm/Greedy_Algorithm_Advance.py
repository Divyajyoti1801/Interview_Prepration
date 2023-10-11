"""
GREEDY ALGORITHM 
"""

"""
General Structure of Greedy Algorithm

    def structure_of_greedy(arr):
        res = 0
        while (All Items are not considered):
            i = selectAnItem()
            if(feasible(i)):
                res += i
        return res
"""

"""
Applications Of Greedy Algorithm
    - Finding Optimal Solution
        = Activity Selection
        = Fractional Knapsack
        = Job Sequencing
        = Prim's Algorithm 
        = Kruskal's Algorithm
        = Dijkstra's Algorithm  
        = Huffman Coding
    - Finding close to optimal coding for NP hard problems like Traveling Salesman Problem.  
"""


"""
Greed Algo - 1
    - Consider infinite supply of the following value of coins
        10  5   2   1
    if someone asks for an amount how will you give this amount using minimum coins.
    - Example : 
        = Amount : 52
        = Take 5 coins of 10 Rs
        = Take 1 coins of 2 Rs
"""
def minimum_coins(coins = [],amount=0):
    coins.sort(reverse=True)
    res = 0
    for x in coins:
        if x <= amount :
            c = amount // x
            res += 1
            amount -= (c * x)
        if amount == 0:
            break
    return res
print("Minimum Coins required to pay for the amount (Naive): ",minimum_coins([5,10,2,1],57))
print()

"""
Greedy Algo - 2
    - Activity selection problem
    - Maximum no. of activities that can happen on a single tasking machine.
        { (2,3) , (1,4) , (5,8) , (6,10) }
        2 tasks at a time

Solution Pseudo Code:
    - Sort according to finish time : 
        {(1,3) , (2,4) , (3,8) , (10,11)}
    - Initialize solution as first activity.
    - Do following for remaining activities:
        = if current activity overlaps with the last picked activity in the solution ignore the current activity
        = else add the current activity to the solution
"""