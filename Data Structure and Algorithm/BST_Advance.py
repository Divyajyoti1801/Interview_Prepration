"""
BINARY SEARCH TREE ADVANCE CONCEPTS AND QUESTIONS
"""
import sys

INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert_node(root,data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_node(root.left,data)
    elif data > root.data:
        root.right = insert_node(root.right,data)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data,end= " ")
        inorder_traversal(root.right)
    else:
        return
"""
Problem Statement: Ceiling on the left size in an array
"""
def ceiling_on_left_1(arr):
    n =len(arr)
    print("-1",end=" ")
    for i in range(1,n):
        diff = sys.maxsize
        for j in range(i):
            if arr[j]>=arr[i]:
                diff = min(diff,arr[j]-arr[i])
        if diff == sys.maxsize:
            print("-1",end = " ")
        else:
            print(arr[i] + diff,end = " ")
print("The Ceiling on the left side O(n^2): ")
ceiling_on_left_1([2,8,30,15,25,12])
print()
def ceiling_on_left_2(arr):
    n = len(arr)
    print("-1",end=" ")
    s = set()
    s.add(arr[0])
    for i in range(1,n):
        it = [x for x in s if x>=arr[i]]
        if len(it) == 0:
            print("-1",end=" ")
        else:
            print(min(it),end=" ")
        s.add(arr[i])
    print()
print("The Ceiling on the left side O(n): ")
ceiling_on_left_2([4,3,30,15,25])
print()
"""
Problem Statement: Find the kth smallest in BST
"""
root_1 = Node(15)
root_1.left = Node(5) # type: ignore
root_1.left.left = Node(3) # type: ignore
root_1.right = Node(20) # type: ignore
root_1.right.left = Node(18) # type: ignore
root_1.right.left.left = Node(16) # type: ignore
root_1.right.right = Node(80) # type: ignore
def kth_smallest_BST_1(root,k):
    if root!=None:
        kth_smallest_BST_1(root.left,k)
        kth_smallest_BST_1.count+=1

        if kth_smallest_BST_1.count == 1:
            print(root.data)
            return
        kth_smallest_BST_1(root.right,k)
print("The Kth Smallest in BST(Naive): ",end=" ")
kth_smallest_BST_1.count = 0
K_smallest = 3
kth_smallest_BST_1(root_1,K_smallest)

def kth_smallest_BST_2(root):
    global K_smallest
    if root is None:
        return None
    left = kth_smallest_BST_2(root.left)
    if left!= None:
        return left
    K_smallest -=1
    if K_smallest == 0:
        return root
    return kth_smallest_BST_2(root.right)
root_2  = None
data_1 = [20,8,22,4,12,10,14]
for x in data_1:
    root_2 = insert_node(root_2,x)
k = 3
res = kth_smallest_BST_2(root_2)
print("The Kth smallest in BST (Efficient): ",res.data) #type:ignore
print()
"""
Problem Statement: Check for Binary Search Tree
"""
root_3 = Node(4)
root_3.left = Node(2) # type: ignore
root_3.right = Node(5) # type: ignore
root_3.left.left = Node(1) # type: ignore
root_3.left.right = Node(3) # type: ignore
def check_BST_helper(node,min_i,max_i):
    if node is None:
        return True
    if node.data < min_i or node.data > max_i:
        return False
    return check_BST_helper(node.left,min_i,node.data-1) and check_BST_helper(node.right,node.data+1,max_i)
def check_BST_1(node):
    return check_BST_helper(node,INT_MIN,INT_MAX)
print("Check for BST (Naive): ",check_BST_1(root_3))
prev_check_BST=INT_MIN
def check_BST_2(root):
    global prev_check_BST
    if root == None:
        return True
    if check_BST_2(root.left) == False:
        return False
    if root.data <= prev_check_BST:
        return False
    prev_check_BST = root.data
    return check_BST_2(root.right)
print("Check for BST(Efficient): ",check_BST_2(root_3))
print()
"""
Problem Statement: Fix BST with two nodes swapped
"""
root_4 = Node(6)
root_4.left = Node(10) # type: ignore
root_4.right = Node(2) # type: ignore
root_4.left.left = Node(1) # type: ignore
root_4.left.right = Node(3) # type: ignore
root_4.right.left = Node(7) # type: ignore
root_4.right.right = Node(12) # type: ignore
def fix_BST_helper(root,first,middle,last,prev):
    if root:
        fix_BST_helper(root.left,first,middle,last,prev)
        if prev[0] and root.data < prev[0].data:
            if not first[0]:
                first[0] = prev[0]
                middle[0] = root
            else:
                last[0] = root
        prev[0] = root
        fix_BST_helper(root.right,first,middle,last,prev)
def fix_BST(root):
    first = [None]
    middle = [None]
    last = [None]
    prev = [None]
    
    fix_BST_helper(root,first,middle,last,prev)
    if first[0] and last[0]:
        first[0].data,last[0].data = last[0].data,first[0].data
    elif first[0] and middle[0]:
        first[0].data,middle[0].data = middle[0].data,first[0].data
print("Inorder Traversal of Normal Tree: ")
inorder_traversal(root_4)
print()
fix_BST(root_4)
print("Inorder Traversal of Corrected BST: ")
inorder_traversal(root_4)
print()
print()
"""
Problem Statement : Pair sum with given Binary Search Tree
"""
root_5 = Node(10)
root_5.left = Node(8) # type: ignore
root_5.right = Node(20) # type: ignore
root_5.left.left = Node(4) # type: ignore
root_5.left.right = Node(9) # type: ignore
root_5.right.left = Node(11) # type: ignore
root_5.right.right = Node(30) # type: ignore
root_5.right.right.left = Node(25) # type: ignore
def pair_sum(root,sum,s):
    if root == None:
        return False
    if pair_sum(root.left,sum,s):
        return True
    if sum-root.data in s:
        print("Pair Found: {} + {} = {}".format(sum-root.data,root.data,sum))
        return True
    else:
        s.add(root.data)
    return pair_sum(root.right,sum,s)

pair_sum_set = set()
print(pair_sum(root_5,33,pair_sum_set))