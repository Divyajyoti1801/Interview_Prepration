"""
Data Structure: BINARY SEARCH TREE
    Major Operations
        - Search : O(log(n))
        - Insert : O(log(n))
        - Delete : O(log(n))
        - Find Closest: O(log(n))
        - Sorted Traversal: O(n)
    
    Binary Search Tree
        - For every node, keys in left size are smaller and keys in right side are greater
        - All keys are typically considered as distinct
        - Like linked list, it is a linked data structures. 
        - Not very cached friendly
"""
root = None
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
"""
Print the element in BST:
    - Depth first Search
        = Preorder Traversal
"""
def traversal_of_tree(root):
    res = []
    if root == None:
        return []
    res.append(root.data)
    res += traversal_of_tree(root.left)
    res += traversal_of_tree(root.right)
    return res
"""
Inset of Element in BST
    - Time Complexity:
    - Auxiliary Space: 
"""
def insert_in_BST(root,data):
    parent = None
    curr = root
    
    while curr!=None:
        parent = curr

        if curr.data == data:
            return root
        elif curr.data < data:
            curr = curr.left
        else:
            curr =  curr.right
    
    if parent == None:
        return Node(data)
    
    if parent.data > data:
        parent.left = Node(data)
    else:
        parent.right = Node(data)
    
    return root
root = insert_in_BST(root,10)
root = insert_in_BST(root,5)
root = insert_in_BST(root,15)
root = insert_in_BST(root,12)
root = insert_in_BST(root,18)
print("The Present Binary Search Tree: ",traversal_of_tree(root))
print()

"""
Search of Element in BST
    - Time Complexity: O(height of the tree)
    - Auxiliary Space: O(height of the tree)
"""
def search_in_BST(root,key):
    if root == None:
        return False
    elif root.data == key:
        return True
    elif root.data < key:
        return search_in_BST(root.right,key)
    else:
        return search_in_BST(root.left,key)
print("Search in BST: ",search_in_BST(root,40))
print()