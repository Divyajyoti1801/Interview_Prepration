"""
List Advance Concepts
"""
"""
Problem Statement: Left rotate by d places
I/P: l = [1,2,3,4,5] d = 2
O/P: [3,4,5,1,2]
"""
#Slicing Method
def left_rotate(l,d):
    if len(l)<=0:
        return l
    l = l[d:]+l[:d]
    return l
print("Left rotate the list by d (Slicing Method): ",left_rotate([1,2,3,4,5],2))
# Deque Method
from collections import deque
def left_rotate_2(l,d):
    if len(l)<=0:
        return l
    dq = deque(l)
    dq.rotate(-d)
    l = list(dq)
    return l
print("Left rotate the list by d (Deque Method): ",left_rotate_2([1,2,3,4,5],2))
# Recursive Method
def reversal(l,a,b):
    while a<b:
        l[a],l[b]=l[b],l[a]
        a += 1
        b -= 1

def left_rotate_3(l,d):
    n = len(l)
    reversal(l,0,d-1)
    reversal(l,d,n-1)
    reversal(l,0,n-1)
list_1 = [1,2,3,4,5]
left_rotate_3(list_1,2)
print("Left rotate the list by d (Recursive Method): ",list_1)
print()

"""
Problem Statement: Maximum difference problem is to find the maximum of arr[j]-arr[i] where j>i
I/P: arr = [2,3,10,6,4,8,1]
O/P: 8
Time Complexity: O(n)
"""
def maximum_difference(l):
    if len(l)<=0:
        return -1
    res = l[1] - l[0]
    min_val = l[0]
    for j in range(1,len(l)):
        res = max(res,l[j] - min_val)
        min_val = min(l[j],min_val)
    return res
print("Maximum difference (Efficient): ",maximum_difference([2,3,10,6,4,8,1]))
print()
"""
Problem Statement: Stock buy and sell. Calculate total profit.
I/P : [1,5,3,8,12]
O/P : 13

Naive Algorithm:
    - Consider every pair (Xi,Xj) such that
        = j > i
        = Xj > Xi
    - Profit with this pair considered is:
        = (xj - xi) + maxProfit(0,i-1) + maxProfit(j+1,n-1)
Efficient Algorithm:
    - Time Complexity : O(n)
"""
def buy_and_sell_1(l,b,e):
    if e<=b:
        return 0
    res = 0
    for i in range(b,e):
        for j in range(i+1,e+1):
            if l[j]>l[i]:
                curr = l[j] - l[i] + buy_and_sell_1(l,0,i-1) + buy_and_sell_1(l,j+1,e)
                res = max(res,curr)
    return res
print("Buy and sell stock for maximum profit (Naive): ",buy_and_sell_1([1,5,3,8,12],0,4))

def buy_and_sell_2(l):
    profit = 0
    for i in range(1,len(l)):
        if l[i]>l[i-1]:
            profit += l[i] - l[i-1]
    return profit
print("Buy and sell stock for maximum profit (efficient): ",buy_and_sell_2([1,5,3,8,12]))
print()

"""
Problem Statement: Tapping rain water problems
I/P: [2,0,2]
O/P: 2
"""
def tapping_rainwater_1(l):
    res = 0
    j=0
    for i in range(1,len(l)-1):
        left_max = l[i]
        for j in range(0,i):
            left_max= max(left_max,l[j])
        right_max = l[j]
        for j in range(i+1,len(l)):
            right_max = max(right_max,l[j])
        res+= min(left_max,right_max)-l[i]
    return res
print("Tapping Rainwater (Naive) O(n^2): ",tapping_rainwater_1([2,0,2]))
def tapping_rainwater_2(l):
    res = 0
    left_max = [0] * len(l)
    right_max = [0] * len(l)
    left_max[0] = l[0]
    for i in range(1,len(l)):
        left_max[i] = max(l[i],left_max[i-1])
    right_max[len(l)-1] = l[len(l)-1]
    for i in range(len(l)-2,-1,-1):
        right_max[i] = max(l[i], right_max[i+1])
    for i in range(1,len(l)-1):
        res += min(left_max[i],right_max[i])-l[i]
    return res
print("Tapping Rainwater (Efficient): ",tapping_rainwater_2([2,0,2]))
print()

"""
Problem Statement: Maximum subarray sum 
I/P: l = [2,3,-8,7,-1,2,3]
O/P: 11
"""
def max_subarray_sum_1(l):
    res = 0
    for i in range(0,len(l)):
        curr = 0
        for j in range(i,len(l)):
            curr+= l[j]
            res = max(res,curr)
    return res
print("Maximum Subarray sum (Naive) O(n^2): ",max_subarray_sum_1([2,3,-8,7,-1,2,3]))

def max_subarray_sum_2(l):
    res = l[0]
    max_ending = l[0]
    for i in range(1,len(l)):
        max_ending = max(max_ending + l[i],l[i])
        res = max(max_ending,res)
    return res
print("Maximum Subarray sum (Efficient) O(n): ",max_subarray_sum_2([2,3,-8,7,-1,2,3]))
print()

"""
Problem Statement : Longest Even Odd Subarray
I/P: [10,12,14,7,8]
O/P: 3
"""