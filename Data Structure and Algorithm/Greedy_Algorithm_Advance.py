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
Time Complexity: O(nlog(n))
"""
def max_activities(arr):
    n = len(arr)
    arr.sort(key = lambda x:x[1])
    prev = 0
    res = 1
    for curr in range(1,n):
        if arr[curr][0]>=arr[prev][1]:
            res += 1
            prev = curr
    return res
print("Maximum no. of activities that can happen on a single machine: ",max_activities([(12,25),(10,20),(20,30)]))
print()
"""
Greedy Algo - 3 
    - Fractional Knapsack Problem
    Weights : 50    20    30
    Values  : 600   500   400
    
    Knapsack Capacity : 70
    Find the maximum value we can obtain in a knapsack.

Pseudo Code:
    - Calculate ratio (value/weight) for every item.
    - Sort all item in decreasing order of the ratio.
    - Initialize : res = 0, curr_cap = given_cap
    - Do following for every item I in sorted order
        = Else if (I.wight <= curr_cap)
            {
                curr_cap -= I.weight
                res += I.value
            }
        = Else
            {
                res += (I.value) * (curr.cap/I.weight);
                return res
            }
        = Return res

Time Complexity : O(nlog(n)) 
"""
def fractional_knapsack(knapsack,arr):
    n = len(arr)
    cost_weight = []
    
    for i in range(n):
        c , W = arr[i][0],arr[i][1]
        cost_weight.append((c,W,((c*1.0)/knapsack)))
    
    cost_weight = sorted(cost_weight,key=lambda x:x[2],reverse=True)
    
    res = 0.0

    for curr in cost_weight:
        if curr[1] <= knapsack:
            res += curr[0]
            knapsack -= curr[1]
        else:
            res+=(curr[0]*(knapsack/curr[1]))
            break
    return res
print("Fractional Knapsack problem : ",fractional_knapsack(50,[(120,30),(100,20),(60,10)]))
print()

"""
Greedy Algo - 4
    - Job Sequencing Problem
    Deadline : 4    1   1   1
    Profit   : 70   80  30  100 

Rules:
    - One Unit per job
    - Only one job can be assigned at time.
    - Time start with zero.

Pseudo Code :
    - Sort the jobs in decreasing order
    - Add the jobs to the latest possible slot
    - if jobs cannot be added ignore it
"""
def job_scheduling(arr,t):
    n = len(arr)
    arr.sort(key = lambda x:x[1],reverse=True)
    result = [False] * t
    res = 0

    for i in range(n):
        for j in range(min(t-1,arr[i][0]-1),-1,-1):
            if result[j] == False:
                result[j] = True
                res += arr[i][1]
                break
    return res
print("Job Sequencing Problem: ",job_scheduling([(4,50),(1,5),(1,20),(5,10),(5,80)],5))
print()

"""
Greed Algo - 5 :
    - Huffman Coding
    - Used for lossless compression
    - Variable length coding

"""