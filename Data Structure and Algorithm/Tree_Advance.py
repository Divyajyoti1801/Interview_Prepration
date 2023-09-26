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
print()

"""
Problem Statement: Construct Binary Tree from InOrder and PreOrder
"""
pre_index = 0
mp={}
def build_tree_with_inorder_postorder(inorder,preorder,index_start,index_end):
    global pre_index,mp
    if index_start>index_end:
        return None
    
    curr = preorder[pre_index]
    pre_index +=1
    temp_node = Node(curr)
    
    if index_start == index_end:
        return temp_node
    
    inorder_index = mp[curr]

    temp_node.left = build_tree_with_inorder_postorder(inorder,preorder,index_start,inorder_index-1) # type: ignore
    temp_node.right = build_tree_with_inorder_postorder(inorder,preorder,inorder_index+1,index_end) # type: ignore
    return temp_node

def build_tree_wrap(inorder,preorder,length):
    global mp
    for i in range(length):
        mp[inorder[i]] = i
    return build_tree_with_inorder_postorder(inorder,preorder,0,length-1)

def inorder_traversal(node):
    if node == None:
        return
    inorder_traversal(node.left)
    print(node.data,end = " ")
    inorder_traversal(node.right)
print("Constructing Binary Tree from InOrder and PreOrder arrangement O(n)")
inOrder_array = ["D","B","E","A","F","C"]
preOrder_array = ["A","B","D","E","C","F"]
root = build_tree_wrap(inOrder_array,preOrder_array,len(inOrder_array))
inorder_traversal(root)
print()
print()
"""
Problem Statement: Tree Traversal in Spiral Form

    Method 1 (Use a Queue and a Stack)
        = We use line by line traversal idea. to reverse the alternate levels, we use a stack
        = Alternate level node are first pushed into a stack then printed
    
    Method 2:
        = Push root to the stack_1
        = While any of the two stacks is not empty
            - While stack_1 is not empty
                = Take out a node, print it
                = Push children of the taken out node into stack_2
            - While stack_2 is not empty
                = Take out a node, print it
                = Push children of the taken out node into stack_1 order
"""
def tree_traversal_in_spiral_form(root):
    h = height_of_tree(root)
    ltr = False
    for i in range(1,h+1):
        level_traversal(root,i,ltr)
        ltr = not ltr

def level_traversal(root,level,ltr):
    if root == None:
        return
    if level == 1:
        print(root.data,end=" ")
    elif level>1:
        if ltr:
            level_traversal(root.left,level-1,ltr)
            level_traversal(root.right,level-1,ltr)
        else:
            level_traversal(root.right,level-1,ltr)
            level_traversal(root.left,level-1,ltr)
print("Spiral Order traversal of Binary Tree: ")
root_6 = Node(1)
root_6.left = Node(2) # type: ignore
root_6.right= Node(3) # type: ignore
root_6.left.left= Node(7) # type: ignore
root_6.left.right= Node(6) # type: ignore
root_6.right.left= Node(5) # type: ignore
root_6.right.right= Node(4) # type: ignore
tree_traversal_in_spiral_form(root_6)
print()
print()
"""
Problem Statement: Diameter of a Binary Tree
    Better Solution: O(n) Time use a dictionary
        - Pre Compute heights of all nodes by calling the recursive height function
        - Store these heights in a dictionary with node as a key and height as a value.
        - The Recursive diameter function simply precomputed value
"""
root_7 = Node(1)
root_7.left = Node(2) # type: ignore
root_7.right = Node(3) # type: ignore
root_7.left.left = Node(4) # type: ignore
root_7.left.right = Node(5) # type: ignore

def diameter_binary_tree_1(root):
    if root is None:
        return 0
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    left_diameter = diameter_binary_tree_1(root.left)
    right_diameter = diameter_binary_tree_1(root.right)

    return max(left_height+right_height+1,max(left_diameter,right_diameter))
print("Diameter of a Binary Tree 1: ",diameter_binary_tree_1(root_7))
class Height:
    def __init__(self):
        self.h = 0

def diameter_binary_tree_2(root,height):
    left_height = Height()
    right_height = Height()
    if root is None:
        height.h = 0
        return 0
    left_diameter = diameter_binary_tree_2(root.left,left_height)
    right_diameter = diameter_binary_tree_2(root.right,right_height)
    
    height.h = max(left_height.h,right_height.h) + 1
    return max(left_height.h+right_height.h+1,max(left_diameter,right_diameter))

def diameter_2(root):
    height = Height()
    return diameter_binary_tree_2(root,height)
print("Diameter of a Binary Tree 2: ",diameter_2(root_7))
print()

"""
Problem Statement : Lowest Common Ancestor (LCA)

    Efficient Solution: Require one traversal. We have the following cases for every node.
        - If it is same as node_1 or node_2
        - If one of the subtrees contains node_1 and other contains node_2
        - If one of the subtrees contains both node_1 and node_2
        - If none of its subtrees contain any of node_1 and node_2
"""
def find_path(root,path,x):
    if root is None:
        return False
    path.append(root.data)
    if root.data == x:
        return True
    if (root.left!=None and find_path(root.left,path,x)) or (root.right!=None and find_path(root.right,path,x)):
        return True
    path.pop()
    return False

def lowest_common_ancestor_1(root,node_1,node_2):
    path_1 = []
    path_2 = []
    if not find_path(root,path_1,node_1) or not find_path(root,path_2,node_2):
        return None
    i = 0
    while i<len(path_1) and i<len(path_2):
        if path_1[i]!=path_2[i]:
            break
        i+=1
    return path_1[i-1]
root_8 = Node(10)
root_8.left = Node(20) # type: ignore
root_8.right = Node(30) # type: ignore
root_8.right.left = Node(40) # type: ignore
root_8.right.right = Node(50) # type: ignore
print("Lowest Common Ancestor 1: ",lowest_common_ancestor_1(root_8,20,50))

def lowest_common_ancestor_2(root,node_1,node_2):
    if root is None:
        return None
    if root.data == node_1 or root.data==node_2:
        return root
    lca_1 = lowest_common_ancestor_2(root.left,node_1,node_2)
    lca_2 = lowest_common_ancestor_2(root.right,node_1,node_2)
    if lca_1 and lca_2:
        return root
    return lca_1 if lca_1 else lca_2
print("Lowest common ancestor 2: ",lowest_common_ancestor_2(root_8,20,50).data) #type:ignore
print()

"""
Problem Statement: Burn a Binary tree from a leaf
"""
root_9 = Node(10)
root_9.left = Node(20) # type: ignore
root_9.right = Node(30) # type: ignore
root_9.right.right = Node(60) # type: ignore
root_9.left.left = Node(40) # type: ignore
root_9.left.right = Node(50) # type: ignore
res_burn = 0
def burn_binary_tree(root,leaf,dist):
    global res_burn
    if root is None:
        return 0
    if root.data == leaf:
        dist[0] = 0
        return 1
    left_dist,right_dist = [-1],[-1]
    lh = burn_binary_tree(root.left,leaf,left_dist)
    rh = burn_binary_tree(root.right,leaf,right_dist)
    if left_dist[0]!=-1:
        dist[0] = left_dist[0] + 1
        res_burn = max(res_burn,rh+dist[0])
    elif right_dist[0] != -1:
        dist[0] = right_dist[0] + 1
        res_burn = max(res_burn,lh + dist[0])
    return max(lh,rh)+1
print("Burn a binary tree from a leaf: ",burn_binary_tree(root_9,50,[-1]))