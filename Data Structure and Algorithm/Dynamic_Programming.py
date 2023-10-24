"""
DYNAMIC PROGRAMMING
"""
import sys
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
        memoization[n] = n # type: ignore
    else:
        memoization[n] = fibonacci_DP_1(n-1) + fibonacci_DP_1(n-2)  # type: ignore
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
print()
"""
DP - 5 :
    - Minimum coins to make a value
    - I/P : coin = [25,10,5], val = 30  ; O/P : 2

Idea for the Recursive solution:
    - if coin[i] > val: Ignore the coin
    - Else:
        = Recursively call for val - coin[i] as new value
        = Update the result if required
"""
def Minimum_Coins_For_Value_Recursive(coin,val):
    if val == 0:
        return 0 
    n = len(coin)
    res = -1
    for i in range(n):
        if coin[i] <= val:
            sub_res = Minimum_Coins_For_Value_Recursive(coin,val-coin[i])
            if sub_res!=-1:
                if res == -1 or (sub_res+1)<res:
                    res= sub_res + 1
    return res
print("Minimum Coins for value (Recursive): ",Minimum_Coins_For_Value_Recursive([25,10,5],30))
print()

"""
DP - 6 :
    - Minimum jumps to reach end
    - I/P : arr = [3,4,2,1,2,1] ; O/P : 2
"""
def Minimum_Jumps_To_Reach_End(arr,n):
    if n == 1:
        return 0
    res = sys.maxsize
    for i in range(n-1):
        if i + arr[i] >= n-1:
            sub_res = Minimum_Jumps_To_Reach_End(arr,i+1)
            if sub_res!= sys.maxsize:
                res = min(res,sub_res+1)
    return res
print("Minimum Jumps To Reach End (Recursive) : ",Minimum_Jumps_To_Reach_End([3,4,2,1,2,1],len([3,4,2,1,2,1])))
def Minimum_Jumps_To_Reach_End_Iterative(arr):
    n = len(arr)
    dp=[sys.maxsize] * n
    dp[0] = 0
    for i in range(1,n):
        for j in range(i):
            if (i<=j + arr[j]) and dp[j] != sys.maxsize:
                dp[i] = min(dp[i],dp[j]+1)
                break
    return dp[n-1]
print("Minimum Jumps To Reach End (Iterative) : ",Minimum_Jumps_To_Reach_End_Iterative([3,4,2,1,2,1]))
print()

"""
DP - 7 :
    - 0/1 Knapsack Problem
    - v=[10,40,30,50], w = [5,4,6,3] W = 10

DP-Solution:
    - KS(W,wt,val,n) = { 0 : if n==0 or W==0;
                         KS(W,wt,val,n-1) if wt[n-1]>W;
                         max(KS(W,wt,val,n-1),KS*(W-wt[n-1],wt,val,n-1)+val[n-1])                    
                        }
"""
def KnapSack_Recursive(W,wt,val,n):
    if n==0 or W==0:
        return 0
    if wt[n-1]>W:
        return KnapSack_Recursive(W,wt,val,n-1)
    else:
        return max(val[n-1]+KnapSack_Recursive(W-wt[n-1],wt,val,n-1),KnapSack_Recursive(W,wt,val,n-1))
DP_array_1 =[10,40,30,50]
print("Knapsack Problem (Recursive): ",KnapSack_Recursive(10,[5,4,6,3],DP_array_1,len(DP_array_1)))

def KnapSack_Iterative(W,wt,val):
    n = len(wt)
    dp = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<= j:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-wt[i-1]]+val[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]
print("Knapsack Problem (Tabulation): ",KnapSack_Iterative(10,[5,4,6,3],DP_array_1))
print()

"""
DP - 8 :
    - Optimal Strategy for a game
    - I/P : arr = [20,5]; O/P : 20
    - Rules
        = Two player game
        = Both players get turns one by one
        = Give No. of Coins is even initially
        = You always make the first move.
        = Both player play optimally

1st Recursive Solution:
    - We find the sum of values before recursive calls.
    - We make two recursive calls and take the maximum of two:
        - Pick the left corner coin 
        - Pick the right corner coin
    - Idea of the the recursive - Sum optimal value that opponent can get the remaining coins

Tabulation Solution : 
    dp[i][j] = {
                    max(arr[i],arr[j]) if i+1=j;
                    max{
                        arr[i] + min(dp[i+2][j],dp[i+1][j-1]),
                        arr[j] + min(dp[i+1]pj-1),dp[i][j-2])
                        }
               }
    dp[0][n-1] is the final result
"""
def Optimal_Strategy_Recursive_1(arr):
    return Optimal_Strategy_Utility_1(arr,0,len(arr)-1,sum(arr))
def Optimal_Strategy_Utility_1(arr,i,j,sum):
    if i+1 == j:
        return max(arr[i],arr[j])
    return max(sum-Optimal_Strategy_Utility_1(arr,i+1,j,sum-arr[i]),sum - Optimal_Strategy_Utility_1(arr,i,j-1,sum-arr[j]))
print("Optimal Strategy for the game (Recursive-1): ",Optimal_Strategy_Recursive_1([8,15,7,3]))

def Optimal_Strategy_Recursive_2(arr,i,j):
    if i+1 == j:
        return max(arr[i],arr[j])
    return max(min(Optimal_Strategy_Recursive_2(arr,i+2,j),Optimal_Strategy_Recursive_2(arr,i+1,j-1)+arr[i]),min(Optimal_Strategy_Recursive_2(arr,i+1,j-1),Optimal_Strategy_Recursive_2(arr,i,j-2)+arr[j]))
print("Optimal Strategy for the game (Recursive-2): ",Optimal_Strategy_Recursive_2([20,5,4,6],0,3))

def Optimal_Strategy_Tabulation(arr):
    n = len(arr)
    dp = [[0 for x in range(n)] for x in range(n)]
    for i in range(n-1):
        dp[i][i+1] = max(arr[i],arr[i+1])
    for gap in range(3,n,2):
        for i in range(n-gap):
            j = i+gap
            dp[i][j] = max(arr[i]+min(dp[i+2][j],dp[i+1][j-1]),arr[j]+min(dp[i+1][j-1],dp[i][j-2]))
    return dp[0][n-1]
print("Optimal Strategy for a game (Tabulation): ",Optimal_Strategy_Tabulation([20,5,4,6,8,3]))
print()

"""
DP - 9
    - Subset Sum Problem
Tabulation Solution : 
    if (j<arr[i-1]){
        dp[i][j] = dp[i-1][j-1]
    else:
        dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    }
"""
def Subset_Sum_Recursive(arr,n,sum):
    if n==0:
        return 1 if sum==0 else 0
    return Subset_Sum_Recursive(arr,n-1,sum)+Subset_Sum_Recursive(arr,n-1,sum-arr[n-1])
print("Subset Sum Problem (Recursive): ",Subset_Sum_Recursive([2,5,3],len([2,5,3]),5))
def Subset_Sum_Tabulation(arr,sum):
    n = len(arr)
    dp = [[0 for x in range(sum+1)] for x in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    return dp[n][sum]
print("Subset Sum Problem (Tabulation): ",Subset_Sum_Tabulation([2,5,3],5))
print()

"""
DP - 10
    - Egg Dropping Puzzle : Find Minimum trials in worst case
    - e : No. of Eggs ; f : No. of Floors
    - I/P : e = 1, f = 10 ; O/P : 10
    - Rules to Consider: 
        = Egg may break from 1st Floor
        = Egg may not break from the top floor
        = if an Egg breaks from a floor, it will break from higher floor also.
Algorithm : 
    - Let res(f,e) be the minimum trials in the worst case for 'f' floors and 'e' eggs.
    - res(f,e) = (f)Min(x=1)[Max(Breaks,Does not Break)]+1 ; 1 <= x <= f
"""
def Egg_Drop_Puzzle(n,k):
    if(k==1 or k==0):
        return k
    if(n==1):
        return k
    min = sys.maxsize
    
    for x in range(1,k+1):
        res = max(Egg_Drop_Puzzle(n-1,x-1),Egg_Drop_Puzzle(n,k-x)) # type: ignore
        if res < min:
            min = res
    return min + 1
print("Minimum number of trials in worst case, 2 eggs and 10 floor is",Egg_Drop_Puzzle(2,10))
print()

"""
DP - 11 
    - Matrix Chain Multiplication
    - arr1[n1][m1] * arr2[n2][m2]; only happen if m1 == n2 
    - I/P : [2,1,3,4] ; O/P : 20
    - Input array is the dimension of the matrix
"""
def Matrix_Chain_Multiplication_Recursion(arr,i,j):
    if(i+1==j):
        return 0
    res = float("inf")
    for k in range(i+1,j):
        res = min(res,Matrix_Chain_Multiplication_Recursion(arr,i,k)+Matrix_Chain_Multiplication_Recursion(arr,k,j)+arr[i]*arr[j]*arr[k]) # type: ignore
    return res
print("Matrix Chain Multiplication (Recursion): ",Matrix_Chain_Multiplication_Recursion([2,1,3,4],0,len([2,1,3,4])-1))
def Matrix_Chain_Multiplication_Tabulation(arr):
    n = len(arr)
    dp = [[None for x in range(n)] for x in range(n)]
    for i in range(0,n-1):
        dp[i][i+1] = 0 # type: ignore
    for gap in range(2,n):
        for i in range(0,n-gap):
            j = i+gap
            dp[i][j] =float("inf") # type: ignore
            for k in range(i+1,j):
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j]+arr[i]*arr[k]*arr[j]) # type: ignore
    return dp[0][n-1]
print("Matrix Chain Multiplication (Tabulation): ",Matrix_Chain_Multiplication_Tabulation([2,1,3,4]))
print()

"""
DP - 12
    - Count Binary-Search-Tree with n keys.
    - I/P: n = 1 ; O/P : 1
"""
def factorial_utility(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

def binomial_coefficient_utility(n,k):
    res = 1
    if k>n-k:
        k = n-k
    for i in range(k):
        res *= (n-i)
        res //= (i+1)
    return res

def catalan_number_utility(n):
    c = binomial_coefficient_utility(2*n,n)
    return c // (n+1)

def Count_BST(n):
    count = catalan_number_utility(n)
    return count

def Count_Binary_Tree(n):
    count = catalan_number_utility(n)
    return count * factorial_utility(n)
print("Count of BST with 5 node is ",Count_BST(5))
print("Count of Binary Trees with 5 node is : ",Count_Binary_Tree(5))
print()