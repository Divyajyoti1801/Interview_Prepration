"""
DYNAMIC PROGRAMMING
"""
"""
Introduction
    - In simple words, it is an organization over plain recursion.
    - The idea is to reuse the solution of sub-problems when there are overlapping subproblem.
        = Memoization (top-down)
        = Tabulation (bottom-up)
"""
"""
Application
    - Bellman Ford Algorithm
    - Floyd warshall  Algorithm 
    - Diff utility (Longest Common Subsequence)
    - Search Closed Words (Edit Distance)
    - Resource Allocation (0-1 Knapsack)
"""
"""
DP Method : Memoization (example)
    - Problem : Fibonacci Number
    - Observation on the above Recursion Tree:
        = We solve same sub-problems again
        = Memoization : Store solution and before proceeding further, check if already completed 
"""
memoization = [None] * 100

def fibonacci_DP_1(n):
    if memoization[n] != None:
        return memoization[n]
    if n == 0 or n == 1:
        memoization[n] = n
    else:
        memoization[n] = fibonacci_DP_1(n-1) + fibonacci_DP_1(n-2)
    return memoization[n]
print("Fibonacci number (Memoization): ",fibonacci_DP_1(6))
"""
DP Method : Tabulation (example)
    - Problem : Fibonacci Series
    - Bottom - Up Approach
"""
def fibonacci_DP_2(n):
    dp = [None] * (n+1)
    dp[0] = 0 
    dp[1] = 1
    for i in range(2,n+1):
        dp[i]= dp[i-1] +dp[i-2]
    return dp[n]
print("Fibonacci Number (Tabulation): ",fibonacci_DP_2(6));
print()
"""
DP - 1 : 
    - Longest Common Subsequence
    - I/P : s1 = "ABCDGH", s2 = "AEDFHR" | O/P : 3

Variation of LCS:
    - Diff Utility
    - Minimum insertions and deletions to convert s1 and s2
    - Shortest Common Super_Sequence
    - Longest Palindromic Sub_Sequence
    - Longest Repeating Sub_Sequence
    - Space Optimized DP solution of DP of LCS
    - Printing LCS
"""
def LCS_Recursive(s1,s2,n,m):
    if m == 0 or n == 0:
        return 0
    if s1[n-1] == s2[m-1]:
        return 1 + LCS_Recursive(s1,s2,n-1,m-1) # type: ignore
    else:
        return max(LCS_Recursive(s1,s2,n,m-1),LCS_Recursive(s1,s2,n-1,m))
print("Longest Common Subsequence (Recursive): ",LCS_Recursive("AXYZ","BAZ",len("AXYZ"),len("BAZ")))

N = 1000
M = 1000

Memo_LCS  = [[-1]*N for i in range(M)]
def LCS_Memoization(s1,s2,n,m):
    if Memo_LCS[n][m]!= -1:
        return Memo_LCS[n][m]
    if n==0 or m==0:
        Memo_LCS[n][m] = 0
    else:
        if s1[n-1]==s2[m-1]:
            Memo_LCS[n][m] = 1 + LCS_Memoization(s1,s2,n-1,m-1)
        else:
            Memo_LCS[n][m] = max(LCS_Memoization(s1,s2,n-1,m),LCS_Memoization(s1,s2,n,m-1))
    return Memo_LCS[n][m]
print("Longest Common Subsequence (Memoization): ",LCS_Memoization("AXYZ","BAZ",len("AXYZ"),len("BAZ")))

def LCS_Tabulation(s1,s2):
    m = len(s1)
    n = len(s2)
    dp = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0 # type: ignore
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1] # type: ignore
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]) # type: ignore
    return dp[m][n]
print("Longest Common Subsequence (Tabulation): ",LCS_Tabulation("AXYZ","BAZ"))
print()

"""
DP - 2 :
    - Coin Change (Count Combination)
    - Infinite supply of every coin type
    - I/P : Coins = [1,2,3] Sum = 4 ; O/P : 4

Idea for the Recursive Solution:
    - We consider two choices for every coin
        = Included
        = Not Included
    - We return sum of the results of the two Recursive calls.

Idea for DP Solution:
    - A (n+1)*(s+1) array where dp[i][j] is going to store result for first i coins and j sum.
    - dp[i][j] = {  1 : if s=0; 
                    0 : if s>0 and n==0; 
                    dp[i-1][j] : if coin[i-1]>j;
                    dp[i-1][j] + dp[i][j-coin[i-1]] : in all other cases
                }
"""
def Coin_Change_Recursive(coin,n,s):
    if s==0:
        return 1
    if s<0:
        return 0
    if n == 0:
        return 0
    return Coin_Change_Recursive(coin,n,s-coin[n-1]) + Coin_Change_Recursive(coin,n-1,s)
print("Coin Change (Recursive): ",Coin_Change_Recursive([2,5,3],3,5))

def Coin_Change_Tabulation(coin,n,s):
    n = len(coin)
    dp = [[0 for x in range(s+1)]for x in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,s+1):
            dp[i][j] = dp[i-1][j]
            if j >= coin[i-1]:
                dp[i][j] += dp[i][j - coin[i-1]]
    return dp[n][s]
print("Coin Change (Tabulation): ",Coin_Change_Tabulation([1,2,3],3,4))
print()

"""
DP - 3 :
    - Edit Distance Problem
    - I/P : s1 = "CAT", s2 = "CUT"; O/P : 1
"""
def Edit_Distance_Recursion(s1,s2,m,n):
    if m == 0 :
        return n
    if n == 0:
        return m
    if s1[m-1] == s2[n-1]:
        return Edit_Distance_Recursion(s1,s2,m-1,n-1)
    else:
        return 1 + min(Edit_Distance_Recursion(s1,s2,m,n-1),Edit_Distance_Recursion(s1,s2,m-1,n),Edit_Distance_Recursion(s1,s2,m-1,n-1))
print("Edit Distance Problem (Recursion): ",Edit_Distance_Recursion("CAT","CUT",3,3))
def Edit_Distance_Tabulation(s1,s2,m,n):
    dp = [[0]*(n+1)for i in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]== s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    return dp[m][n]
print("Edit Distance Problem (Tabulation): ",Edit_Distance_Tabulation("CAT","CUT",3,3))
print()

"""
DP - 4 :
    - Longest Increasing Subsequence
    - I/P : arr = [3,4,2,8,10] O/P : 4

Variation of Longest Increasing Subsequence
    - Minimum deletions to make an array sorted
    
    - Maximum sum Increasing Subsequence 
    
    - Maximum Length of Bitonic Subsequence (First Strictly Increasing then Strictly Decreasing)
        = Algorithm :
            - Build Longest Increasing Subsequence DP
            - Build Longest Decreasing Subsequence DP
            - Find the maximum value of LIS[i] + LDS[i] - 1
    
    - Building Bridges
        = I/P:  [(6,2),(4,3),(2,6),(1,5)] O/P : 2
        = No Crossing Allowed
        = Algorithm: 
            - Sort the array in increasing order of first value of pair. If two first values are same like (2,6) and (2,3), then consider second value.
            - find LIS of the sorted array according to second values.
    
    - The Longest Chain
        - I/P : [(5,24),(39,60),(15,28),(27,40),(50,90)] ; O/P : 3
        - Algorithm :
            = Sort the array on the basis first element.
            = Create the LIS of sorted array
"""
def Longest_Increasing_Subsequence_Tabulation(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1,n):
        for j in range(0,i):
            if arr[i]>arr[j]:
                lis[i] = max(lis[i],lis[j]+1)
    res = lis[0]
    for i in range(n):
        res = max(lis[i],res)
    
    return res
print("Longest Increasing Subsequence (Tabulation): ",Longest_Increasing_Subsequence_Tabulation([3,4,2,8,10,5,1]))
def Longest_Increasing_Subsequence_Efficient(arr):
    n = len(arr)
    tail = [arr[0]]
    for i in range(1,n):
        if arr[i] > tail[-1]:
            tail.append(arr[i])
        else:
            c = ceil_index(tail,arr[i])
            tail[c] = arr[i]
    return len(tail)
def ceil_index(tail,x):
    l = 0
    r = len(tail)-1
    while r>l:
        m = l+(r-l)//2
        if tail[m]>=x:
            r = m
        else:
            l = m + 1
    return r
print("Longest Increasing Subsequence (Efficient): ",Longest_Increasing_Subsequence_Efficient([3,4,2,8,10,5,1]))
"""
DP - 4(2) : LIS Variation - 2
    - Maximum increasing subsequence
    - I/P : [3,1,10,3,4,7] O/P: 14
"""
def Maximum_Increasing_Subsequence(arr):
    max_is = [x for x in arr]
    for i in range(1,len(arr)):
        for j in range(1,i):
            if arr[j] < arr[i]:
                max_is[i] = min(max_is[i], arr[i] + max_is[j])
    return max(max_is)
print("LIS V-1: Maximum Sum of increasing  subsequence: ",Maximum_Increasing_Subsequence([3,1,10,3,4,7]))