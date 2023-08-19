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
def longest_even_odd_subarray_1(l):
    res = 1
    for i in range(0,len(l)):
        curr = 1
        for j in range(i+1,len(l)):
            if (l[j]%2==0 and l[j-1]%2!=0) or (l[j]%2!=0 and l[j-1]%2==0):
                curr+=1
            else:
                break
        res = max(res,curr)
    return res
print("Longest even and odd subarray (Naive) O(n^2): ",longest_even_odd_subarray_1([5,10,20,6,3,8]))

#Kadane's Algorithm
def longest_even_odd_subarray_2(l):
    res = 1
    curr = 1
    for i in range(len(l)):
        if(l[i]%2==0 and l[i-1]%2!=0) or (l[i]%2!=0 and l[i-1]%2==0):
            curr+=1
            res = max(res,curr)
        else:
            curr = 1
    return res
print("Longest even and odd subarray (Efficient) O(n): ",longest_even_odd_subarray_2([5,10,20,6,3,8]))
print()

"""
Problem Statement: Maximum circular subarray sum
I/P: [5,-2,3,4]
O/P: 12

Idea for efficient solution: 
    - Maximum sum of normal subarray:(Kadane's Algorithm)
    - Maximum sum of a circular subarray: Total_sum - maximum_sum_of_subarray
"""
def max_circular_subarray_sum_1(l):
    res = l[0]
    for i in range(0,len(l)):
        curr_max = l[i]
        curr_sum = l[i]
        for j in range(1,len(l)):
            index = (i+j)%len(l) # Circular subarray index
            curr_sum+=l[index]
            curr_max = max(curr_max,curr_sum)
        res = max(res,curr_max)
    return res
print("Maximum sum of all circular subarray (Naive) O(n^2): ",max_circular_subarray_sum_1([5,-2,3,4]))
def max_subarray_sum(l):
    res = l[0]
    max_ending = l[0]
    for i in range(1,len(l)):
        max_ending = max(max_ending+l[i], l[i])
        res = max(max_ending,res)
    return res
def max_circular_subarray_sum_2(l):
    max_normal = max_subarray_sum(l)
    if max_normal<0: # type: ignore
        return max_normal
   
    arr_sum = 0
    for i in range(0,len(l)):
        arr_sum+=l[i]
        l[i]= -l[i]
    max_circular = arr_sum + max_subarray_sum(l) # type: ignore
    return max(max_circular,max_normal) 
print("Maximum sum of all circular subarray (Efficient) O(n): ",max_circular_subarray_sum_2([5,-2,3,4]))
print()

"""
Problem Statement: Find the Majority Element
Majority Element: Majority element is an element that appears more than n/2 times in an array of size n.
I/P: [8,3,4,8,8]
O/P: 0,3,4 (any index of 8)
"""
def majority_element_1(l):
    for i in range(0,len(l)):
        count = 1
        for j in range(i+1,len(l)):
            if l[i] == l[j]:
                count += 1            
        if count>(len(l)/2):
            return i
    return -1
print("The majority element (Naive) O(n^2): ",majority_element_1([8,3,4,8,8]))
# Moore's Voting Algorithm
def majority_element_2(l):
    res = 0
    count = 1
    for i in range(1,len(l)):
        if l[res] == l[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            res = i
            count = 1
    count = 0
    for i in range(0,len(l)):
        if l[res] == l[i]:
            count+=1
    if count <= (len(l)//2):
        res = -1
    return res
print("The majority element (Efficient) O(n): ",majority_element_2([8,3,4,8,8]))
print()

"""
Problem Statement: Given a binary array, we need to find the minimum of number of group flips to make all array elements same.  In a group flip, we can flip any set of consecutive 1s or 0s.

I/P: arr[]  = {1,1,0,0,0,1}
O/P: From 2 to 4
"""
def min_group_flips_1(l):
    for i in range(1,len(l)):
        if l[i] != l[i-1]:
            if l[i] != l[0]:
                print("From ",i," to",end=" ")
            else:
                print(i-1)
    if l[len(l)-1]!=l[0]:
        print(len(l)-1)   
print("Minimum group of flips (efficient): ")
min_group_flips_1([1,1,0,0,0,1])
print()

"""
Problem Statement: Window sliding technique. Find the maximum sun of K consecutive elements
I/P: [1,8,30,-5,20,7] k=3
O/P: 45
"""
def sliding_window_1(l,k):
    res = float("-inf")
    i = 0
    while(i+k-1<len(l)):
        curr = 0
        for j in range(k):
            curr += l[i+j]
        res = max(curr,res)
        i+=1
    return res
print("The maximum sum of K consecutive element (Naive) O(n*k): ",sliding_window_1([1,8,30,-5,20,7],3))
def sliding_window_2(l,k):
    curr = 0
    for i in range(k):
        curr += l[i]
    res = curr
    for i in range(k,len(l)):
        curr = curr + l[i] - l[i-k]
        res = max(res,curr)
    return res
print("The maximum sum of K consecutive element (Efficient) O(n): ",sliding_window_2([1,8,30,-5,20,7],3))
print()

"""
Problem Statement: Subarray with given sum. There are no negative elements in the array.
I/P: [1,4,20,3,5] sum = 33
O/P: Yes
"""
def subarray_with_sum(l,sum):
    s, curr =0,0
    for i in range(len(l)):
        curr += l[i]
        while curr>sum:
            curr -= l[s]
            s += 1
        if curr == sum:
            return True
    return False
print("Is subarray with given sum exists (Efficient) O(n): ",subarray_with_sum([1,4,20,3,10,5],33))
print()

"""
Important Problem Statement: (Prefix Sum Technique)
I/P : arr[] = [2,8,3,9,6,5,4]
      Queries = getSum(0,2), getSum(1,3), getSum(2,6)
O/P : 13 20 27

Idea of Prefix Sum:
    - Pre-compute Prefix Sum Array:
    - getSum(l,r) = { pSum[r] if l == 0; pSum[r]-pSum[l-1] otherwise}
"""
# Very Computation heavy, if Array is very large ~10^5
def prefix_sum_1(l,a,b):
    res = 0
    for i in range(a,b+1):
        res += l[i]
    return res
print("Prefix Sum (naive): ",prefix_sum_1([2,8,3,9,6,5,4],0,2))

def get_sum(pSum,a,b):
    if a == 0:
        return pSum[b]
    else:
        return pSum[b] - pSum[a-1]
    
list_2 = [2,8,3,9,6,5,4]
prefix_sum = [None]*len(list_2)
prefix_sum[0] = list_2[0] # type: ignore
for i in range(1,len(list_2)):
    prefix_sum[i] = prefix_sum[i-1] + list_2[i] # type: ignore
print("Prefix Sum (Efficient): ",get_sum(prefix_sum,2,6))
print()

"""
Important Problem Statement: Find Equilibrium point.
    - Equilibrium Statement : A point is called an equilibrium point if the sum of the left side of the point is equal to the right side of the point in the array.

I/P : arr = [3,4,8,-9,20,6]
O/P : True
"""
def equilibrium_point_1(l):
    n = len(l)
    for i in range(n):
        ls,rs = 0,0
        for j in range(i):
            ls+=l[j]
        for k in range(i+1,n):
            rs+=l[k]
        if ls == rs:
            return True
    return False
print("Equilibrium point (Naive) O(n^2): ",equilibrium_point_1([3,4,8,-9,9,7]))

def equilibrium_point_2(l):
    rs = sum(l)
    ls = 0
    for i in range(len(l)):
        rs -= l[i]
        if ls == rs:
            return True
        ls += l[i]
    return False

print("Equilibrium point (Efficient): ",equilibrium_point_2([3,4,8,-9,9,7]))
print()

"""
Problem Statement: Maximum appearing element in ranges
I/P: left = [1,2,5,15], right = [5,8,7,18]
O/P: 5
"""
def max_appearing_element_1(left,right):
    freq = [0]*100
    for i in range(len(left)):
        for j in range(left[i],right[i]+1):
            freq[j] += 1
    return freq.index(max(freq))
print("Maximum appearing element in ranges (naive): ",max_appearing_element_1([1,2,4],[4,5,7]))

def max_appearing_element_2(left,right):
    freq = [0] * 101
    for i in range(len(left)):
        freq[left[i]]+=1
        freq[right[i]+1] -=1
    for i in range(1,100):
        freq[i] = freq[i] + freq[i-1]
    return freq.index(max(freq))
print("Maximum appearing element in ranges(efficient): ",max_appearing_element_2([1,2,4],[4,5,7]))