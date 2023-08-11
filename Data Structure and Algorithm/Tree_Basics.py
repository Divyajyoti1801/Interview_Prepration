"""
TREE DATA STRUCTURE
    - Non-Linear Data Structure
    - Data Storage in form of Hierarchy
    - Root Node : Head of Hierarchy
    - Recursive in nature
    - Node which have degree 0 are Leaf Nodes

    Applications of Tree Data Structure
        - Organization Structure
        - Folder Structure
        - XML/HTML Content (JSON Objects)
        - In OOP Inheritance 

        - Binary Search Tree
        - Binary Heap
        - B and B+ Trees in DBMS
        - Spanning and Shortest path trees in Computer Networks
        - Parse Tree, Expression Tree in Compiler
        - Trie
        - Suffix Tree
        - Binary Index Tree
        - Segment Tree
"""

"""
Binary Tree Implementation
    - Array Representation 
    - Linked Representation
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)

"""
Binary Tree Traversal
    Methods:
        - Breadth First 
        - Depth First
            = Inorder (Left Root Right)
            = PreOrder (Root Left Right)
            = PostOrder (Left Right Root)
    
    Recursive:
        - Traversal Root
        - Traversal Left Subtree
        - Traversal Right Subtree

    Example Practice : 
        Inorder: 40 20 70 50 80 10 30 60
        Preorder: 10 20 40 50 70 80 30 60
        Postorder: 40 70 80 50 20 60 30 10
"""
root = Node(10)
root.left = Node(20)  # type: ignore
root.right = Node(30)  # type: ignore
root.left.left = Node(40)  # type: ignore
root.left.right = Node(50)  # type: ignore

"""
Traversal Method - Depth First Search
    - Inorder Traversal
    Time Complexity: O(n)
    Auxiliary Space: O(height of the tree)
"""


def inorder_traversal(root):
    if root != None:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)


print("Inorder Traversal of the Binary Tree: ")
inorder_traversal(root)
print()

"""
Traversal Method - Depth First Search
    - Postorder Traversal
    Time Complexity: O(n)
    Auxiliary Space: O(height of the tree)
"""


def postOrder_traversal(root):
    if root != None:
        postOrder_traversal(root.left)
        postOrder_traversal(root.right)
        print(root.data, end=" ")


print("Postorder Traversal of the Binary Tree: ")
postOrder_traversal(root)
print()

"""
Traversal Method - Depth First Search
    - Preorder Traversal
    Time Complexity: O(n)
    Auxiliary Space: O(height of the tree)
"""


def preOrder_traversal(root):
    if root != None:
        print(root.data, end=" ")
        preOrder_traversal(root.left)
        preOrder_traversal(root.right)


print("Preorder Traversal of the Binary Tree: ")
preOrder_traversal(root)
print()

"""
Height of the Binary Tree
    - Conventions
        = Longest root to leave path
        = Maximum Number of Edges 
    
    Time Complexity: O(n)
    Auxiliary Space: O(height of the tree)
"""
def height_of_tree(root):
    if root == None:
        return 0
    else:
        lh = height_of_tree(root.left)
        rh = height_of_tree(root.right)
        return 1 + max(lh,rh) # type: ignore
print("Hight of the Tree(Longest root to leave path): ",height_of_tree(root))
print()
"""
Print Node at K-distance
    Time Complexity: O(n)
    Auxiliary Space: O(1)
"""
def print_k_dist(root,k):
    if root is None:
        return
    if k==0:
        print(root.data,end=" ")
    else:
        print_k_dist(root.left,k-1)
        print_k_dist(root.right,k-1)
print("Print Element from the Kth Distance form root: ")
print_k_dist(root,2)
print()

"""
Traversal Method: Breadth First Search
    - Level Order Traversal
    
    Time Complexity: O(n)
    Auxiliary Space: O(n)
"""
from collections import deque
def level_order_traversal(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while len(q)>0:
        node = q.popleft()
        print(node.data,end =" ")
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
print("Level Order Traversal: ")
level_order_traversal(root)
print()

"""
Size of Binary Tree

    Time Complexity: O(n)
    Auxiliary Space: O(n)
"""
def size_binary_tree(root):
    if root == None:
        return 0
    else:
        ls = size_binary_tree(root.left)
        rs = size_binary_tree(root.right)
        return ls + rs + 1
print("Size of the tree: ",size_binary_tree(root))
print()

"""
Maximum Value of Binary Tree
"""
import math
def max_binary_tree(root):
    if root==None:
        return -math.inf
    else:
        lm = max_binary_tree(root.left)
        rm = max_binary_tree(root.right)
        return max(root.data,lm,rm)
print("Maximum of Binary Tree: ",max_binary_tree(root))
print()