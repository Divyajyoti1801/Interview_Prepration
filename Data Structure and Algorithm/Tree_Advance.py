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

def level_order_traversal(root):
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