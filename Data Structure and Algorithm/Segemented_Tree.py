"""
SEGMENTED TREE ADVANCE DATA STRUCTURE
"""

"""
Introduction

    - Motivation for using segment tree:
        = x/4 : queries of one type : O(n)
        = 3x/4 : queries of other type : O(1)
        = Average Type : [x/4*O(n) + 3x/4*O(1)]/x = O(n)
    
    - Building Segment Tree:
        = left(i) = 2*i + 1
        = right(i) = 2*i + 2
        = parent(i) = (i-1) / 2 
    
    - Size of Tree_Array:
        = if n is a power of two, then 2n-1 else 2x-1 where x is the smallest power of 2 greater than n.
        = Formulae of sizes : 2 * 2^[log2(N)] - 1
"""
"""
Constructing Segment Tree
I/P : arr[] = {10,20,30,40}
O/P : tree[] = {100,30,70,10,20,30,40}

Idea for the Construction:
    - Recursively Build left Subtree
    - Recursively Build right Subtree
    - Fill the root node as sum of left and right children
"""
from turtle import update


arr_1 = [10,20,30,40]
SEGMENT_TREE = [0] *(4*len(arr_1))
def build_segment_tree(ss,se,si):
    if ss == se:
        SEGMENT_TREE[si] = arr_1[ss]
        return arr_1[ss]
    mid = (ss + se) // 2
    SEGMENT_TREE[si] = build_segment_tree(ss,mid,2*si+1) + build_segment_tree(mid+1,se,2*si+2) #type:ignore
    return SEGMENT_TREE[si]
build_segment_tree(0,3,0)
print("The Segment Tree : ",SEGMENT_TREE)
print()

"""
Range Query in Segment Tree : SUM
    Norms:
        - getSumRec(qs,qe,ss,se,si)
            = qs and qe : User Input
            = ss and se : starting and ending indexes of range represented by current node.
            = ss : Index of current node; Initial : si = 0
"""
def range_query_sum(qs,qe,ss,se,si):
    if se<qs or ss>qe:
        return 0
    if qs<=ss and qe>=se:
        return SEGMENT_TREE[si]
    mid = (ss + se) // 2
    return range_query_sum(qs,qe,ss,mid,2*si+1) + range_query_sum(qs,qe,mid+1,se,2*si+2)
print("Range Query - SUM(0,2) : ",range_query_sum(0,2,0,3,0))
print()

"""
Range Query in Segment Tree : UPDATE
Idea for update:
    - Find the difference b/w old and new values
    - Update all the Nodes having given in range
    - We write a recursive function
"""
def range_query_update(ss,se,i,si,diff):
    if i<ss or i>se:
        return
    SEGMENT_TREE[si] += diff
    if se>ss:
        mid = (ss + se)//2
        range_query_update(ss,mid,i,2*si+1,diff)
        range_query_update(mid+1,se,i,2*si+2,diff)
range_query_update(0,3,1,0,5)
print("Range Query - UPDATE(1,5) : ",SEGMENT_TREE)
print()

"""
Binary Indexed Tree
    - Used for fixed input array and multiple queries of the following types:
        = Prefix Operations (Sum, Product, XOR, OR,etc)
        = Update Value
    - It is actually an array, but the concept is Tree Based.
    - Requires O(nlog(n)) preprocessing time and theta(n) auxiliary space.
    - Also known as Fenwick Tree

Prefix Sum Representation:
    - Every number can be expressed as sum of power of 2
    - getSum(13) : Sum of number from arr[0] to arr[13]
    - Implementation (Binary-Index-Tree):
        => i+=1
        => Result = BI_Tree[i] + BI_Tree[parent(i)] + BI_Tree[parent(i)] + ......

"""
arr_2 = [10,20,30,40,50,60,70,80,90]
BINARY_INDEX_TREE = [0] * (len(arr_2)+1)

def Add_Bit_Utility(arr,n,i,v):
    i+=1
    while(i<=n):
        arr[i]+=v
        i+=i&(-i)

def construct_BIT(arr,n):
    for i in range(n):
        Add_Bit_Utility(BINARY_INDEX_TREE,n,i,arr[i])

def prefix_sum_BIT(i):
    i = i+1
    res = 0
    while i>0:
        res = res + BINARY_INDEX_TREE[i]
        i = i - (i&(-i))
    return res
construct_BIT(arr_2,len(arr_2))
print("Binary Index Tree: ",BINARY_INDEX_TREE)
print()
print("The Prefix Sum of BIT: ",prefix_sum_BIT(6))
print()

"""
Update Operation in Binary Index Tree
"""
def update_BIT(i,x):
    i+=1
    while i<=len(BINARY_INDEX_TREE):
        BINARY_INDEX_TREE[i]+=x
        i+=i&(-i)
update_BIT(2,10)
print("Update operation in BIT: ",BINARY_INDEX_TREE)
