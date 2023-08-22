"""
RECURSION ADVANCE PROBLEM
"""

"""
ROPE CUTTING PROBLEM 
Problem Statement 1: Given a rod of length N meters, and the rod can be cut in only 3 sizes A, B and C. The task is to maximizes the number of cuts in rod. If it is impossible to make cut then print -1.

I/P: N = 17 A = 10 B = 11 C = 3
O/P: 3
"""

def rope_cutting_problem(n,a,b,c):
    if n <= -1:
        return -1
    if n == 0:
        return 0
    res  = max(rope_cutting_problem(n-a,a,b,c), rope_cutting_problem(n-b,a,b,c),rope_cutting_problem(n-c,a,b,c))
    
    if res == -1:
        return -1
    return res + 1 # type: ignore

print("Rope cutting problem O(3^n): ",rope_cutting_problem(17,10,11,3))
print()

"""
JOSEPHUS PROBLEM
Problem Statement: Given the total number of persons N and a number k which indicates that k-1 persons are skipped and the kth person is killed in a circle. The task is to choose the person in the initial circle that survives.

I/P: N = 5 and k = 2
O/P: 3
"""
def josephus_problem(n,k):
    if n==1:
        return 1
    else:
        return (josephus_problem(n-1,k)+k-1)% n + 1
print("The person of remains alive: ",josephus_problem(14,2))
print()

"""
Problem Statement: Subset of a string 
I/P: "AB"
O/P: " ","A","B","AB"
"""
def subset_of_string(str,curr,idx):
    if idx == len(str):
        print(curr,end = " ")
        return
    subset_of_string(str,curr,idx+1)
    subset_of_string(str,curr+str[idx],idx+1)
print("The subset of the string: ")
subset_of_string("AB","",0)
print()

"""
Tower of Hanoi
Problem Statement: Tower of Hanoi Problem
I/P: n = 1
O/P: Move disk 1 from A to C  
"""
def tower_of_hanoi(n,S,H,D):
    if n == 1:
        print("Move 1 from ",S, " to ",D)
    else:
        tower_of_hanoi(n-1,S,D,H)
        print("Move ",n," from ",S," to ",D)
        tower_of_hanoi(n-1,H,S,D)

print("Tower of Hanoi: ")
tower_of_hanoi(3, "A","B","C")
print()

"""
Problem Statement: Count subset sum problem 
I/P: [1,2,3,5,6,7], n = 6, sum = 8 
"""
def count_subset_sum(l,n,sum):
    if n == 0:
        if sum == 0:
            return 1
        else:
            return 0
    return count_subset_sum(l,n-1,sum) + count_subset_sum(l,n-1,sum-l[n-1])
print("Count subset sum problem: ",int(count_subset_sum([1,2,3,5,6,7],6,8)))
print()

"""
Problem Statement: Print all Permutations of a string 
I/P: s = "ABC"
O/P: ABC ACB BAC BCA CAB CBA
"""
def permutation_of_string(s, ans):
    if len(s) == 0:
        print(ans, end = " ")
        return
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permutation_of_string(rest,ans + ch)
print("Permutation of a string: ")
permutation_of_string("ABC","")
print()
