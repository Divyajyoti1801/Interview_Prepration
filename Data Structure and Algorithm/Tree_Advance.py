"""
TREE ADVANCE QUESTIONS AND CONCEPTS
"""
from collections import deque
"""
Basic Implementation Reaction
    - Traversal Method
        = Preorder
        = Postorder
        = Inorder
"""
print("Basics Refreshment :")
print()
class Node_Basic:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
# Basic Initialization of Tree 
root = Node_Basic(10)
root.left = Node_Basic(20) # type: ignore
root.right = Node_Basic(30) # type: ignore
root.left.left = Node_Basic(40) # type: ignore
root.left.right = Node_Basic(50) # type: ignore

def basic_inorder_traversal(root):
    if root != None:
        basic_inorder_traversal(root.left)
        print(root.data,end = " ")
        basic_inorder_traversal(root.right)
print("Inorder Traversal Basic of the Binary Tree: ")
basic_inorder_traversal(root)
print()
def basic_postorder_traversal(root):
    if root!=None:
        basic_postorder_traversal(root.left)
        basic_postorder_traversal(root.right)
        print(root.data,end=" ")
print("Postorder traversal basic of Binary Tree: ")
basic_postorder_traversal(root)
print()
def basic_preorder_traversal(root):
    if root!=None:
        print(root.data,end=" ")
        basic_preorder_traversal(root.left)
        basic_preorder_traversal(root.right)       
print("Preorder traversal basic of Binary Tree: ")
basic_preorder_traversal(root)
print()
def basic_height_of_tree(root):
    if root ==None:
        return 0
    else:
        lh = basic_height_of_tree(root.left)
        rh = basic_height_of_tree(root.right)
        return 1 + max(lh,rh)
print("Height of the tree(Longest root to leave path): ",basic_height_of_tree(root))
print()
print()
print("----------------------------------------------")
print()

"""
Advance Concepts
"""
print("Advance Concepts")
print()

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
root_1 = Node(10)
root_1.left = Node(20) # type: ignore
root_1.right = Node(30) # type: ignore
root.left.left = Node(30) # type: ignore

"""
Level Order Traversal Method-1
"""
def level_order_traversal_1(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    q.append(None)
    while len(q)>1:
        curr = q.popleft()
        if curr==None:
            print()
            q.append(None)
            continue
        print(curr.data,end = " ")
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)
print("Level Order Traversal 1: ")
level_order_traversal_1(root_1)
print()
"""
Level Order Traversal Method-2
"""
def level_order_traversal_2(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while len(q)>0:
        count = len(q)
        for i in range(count):
            curr = q.popleft()
            print(curr.data,end = " ")
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        print()
print("Level Order Traversal 2: ")
level_order_traversal_2(root_1)
print()
"""
Problem Statement: Check for Balanced Tree
"""
root_2 = Node(1)
root_2.left = Node(2) # type: ignore
root_2.right = Node(3) # type: ignore
root_2.left.left = Node(4) # type: ignore
root_2.left.right = Node(5) # type: ignore
root_2.left.left.left = Node(8) # type: ignore

def height_of_tree(root):
    if root == None:
        return 0
    else:
        lh = height_of_tree(root.left)
        rh = height_of_tree(root.right)
        return 1 + max(lh,rh)

def check_for_balanced_tree_1(root):
    if root == None:
        return True
    lh = height_of_tree(root.left)    
    rh = height_of_tree(root.right)    
    if (abs(lh - rh) <=1 ) and check_for_balanced_tree_1(root.left) is True and check_for_balanced_tree_1(root.right) is True:
        return True
    return False
print("Checked for balance tree (Naive): ",check_for_balanced_tree_1(root_2))

def check_for_balanced_tree_2(root):
    if root is None:
        return True
    lh = check_for_balanced_tree_2(root.left)
    if lh == -1:
        return -1
    
    rh = check_for_balanced_tree_2(root.right)
    if rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1
    
    else:
        return max(lh,rh)+1

print("Checked for balanced tree (Efficient): ",check_for_balanced_tree_2(root_2))
print()

"""
Problems Statement: Vertical Traversal of a Tree
"""
root_3 = Node(1)
root_3.left = Node(2) # type: ignore
root_3.right = Node(3) # type: ignore
root_3.left.left = Node(4) # type: ignore
root_3.left.right = Node(5) # type: ignore
root_3.right.left = Node(6) # type: ignore
root_3.right.right = Node(7) # type: ignore
root_3.right.left.right = Node(8) # type: ignore
root_3.right.right.right = Node(9) # type: ignore

def find_min_max(node,minimum,maximum,hd):
    if node == None:
        return
    if hd<minimum[0]:
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd
    find_min_max(node.left,minimum,maximum,hd-1)
    find_min_max(node.right,minimum,maximum,hd+1)

def display_vertical_line(node,line,hd):
    if node == None:
        return
    if hd == line:
        print(node.data,end = " ")
    display_vertical_line(node.left,line,hd-1)
    display_vertical_line(node.right,line,hd+1)

def vertical_traversal_tree(root):
    minimum = [0]
    maximum = [0]
    find_min_max(root,minimum,maximum,0)
    for line in range(minimum[0],maximum[0]+1):
        display_vertical_line(root,line,0)
        print()

print("Vertical Traversal Of Tree: ")
vertical_traversal_tree(root_3)
print()

"""
Problem Statement : Bottom view of a Binary Tree
"""
root_4 = Node(20)
root_4.left = Node(8) # type: ignore
root_4.right = Node(22) # type: ignore
root_4.left.left = Node(5) # type: ignore
root_4.left.right = Node(3) # type: ignore
root_4.right.left = Node(4) # type: ignore
root_4.right.right = Node(25) # type: ignore
root_4.left.right.left = Node(10) # type: ignore
root_4.left.right.right = Node(14) # type: ignore

def bottom_view_of_tree(root):
    if root == None:
        return
    hd = 0
    min_hd,max_hd = 0,0
    hd_dict = dict()
    q = deque()
    root.hd = hd
    q.append(root)
    
    while q:
        curr_node = q.popleft()
        hd = curr_node.hd
        min_hd = min(min_hd,hd)
        max_hd = max(max_hd,hd)
        hd_dict[hd] = curr_node.data

        if curr_node.left:
            curr_node.left.hd = hd - 1
            q.append(curr_node.left)
        if curr_node.right:
            curr_node.right.hd = hd + 1
            q.append(curr_node.right)
    
    for i in range(min_hd,max_hd+1):
        print(hd_dict[i],end=" ")
    

print("Bottom view of a Binary Tree: ")
bottom_view_of_tree(root_4)
print()
print()
"""
Problem Statement: Maximum width of Binary Tree
    Idea for Solution:
        - We use line by line level order traversal concept
"""
def max_width_of_tree(root):
    if root==None:
        return None
    q = deque()
    q.append(root)
    res = 0
    while q:
        count = len(q)
        for i in range(count):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res = max(res,count)
    return res
print("The Maximum width of the binary tree: ",max_width_of_tree(root_4))
print()

"""
Problem Statement : Convert a Binary Tree to Doubly Linked List
"""
root_5 = Node(10)
root_5.left = Node(12) # type: ignore
root_5.right = Node(15)  # type: ignore
root_5.left.left = Node(25)  # type: ignore
root_5.left.right = Node(30)  # type: ignore
root_5.right.left = Node(36)  # type: ignore
prev_link = None

def binary_tree_to_linked_list(root):
    if root is None:
        return root
    head = binary_tree_to_linked_list(root.left)
    global prev_link
    if prev_link is None:
        head = root
    else:
        root.left = prev_link
        prev_link.right = root
    prev_link = root
    binary_tree_to_linked_list(root.right)
    return head
def traverse_linked_list(head):
    while head is not None:
        print(head.data,end = " ")
        head = head.right
print("Conversion of Binary Tree into Doubly Linked list: ")
traverse_linked_list(binary_tree_to_linked_list(root_5))
print()

"""
Problem Statement: Construct Binary Tree from InOrder and PreOrder
"""
# mp ={}
# preIndex = 0
# def build_tree_with_preorder_inorder(preorder,inorder,index_start,index_end):
#     global preIndex,mp
#     if index_start > index_end:
#         return None
#     curr = preorder[preIndex]
#     preIndex+=1
#     temp_node = Node(curr)
#     temp_node.left = build_tree_with_preorder_inorder(preorder,inorder,index_start,index_end-1)
#     temp_node.right = build_tree_with_preorder_inorder(preorder,inorder,temp_node+1)