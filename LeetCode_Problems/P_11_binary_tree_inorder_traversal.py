"""
Problem - 11 : BINARY TREE INORDER TRAVERSAL

Problem Statement:
    - Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,3,2]
"""
class TreeNode:
    def __init__(self,data=0):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(root):
    return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right) if root else []


print("Inorder Traversal : ",)
