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