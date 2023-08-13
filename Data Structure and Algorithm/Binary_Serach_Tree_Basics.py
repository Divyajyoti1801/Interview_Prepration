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
    if not root:
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
    if root == None:
        return Node(data)
    elif root.data == data:
        return root
    elif root.data > data:
        root.left = insert_in_BST(root.left,data)
    else:
        root.right = insert_in_BST(root.right,data)
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
print("Search in BST: ",search_in_BST(root,15))
print()

"""
Deletion of Element in BST
    - Time Complexity: O(height of the tree)
    - Auxiliary Space: O(height of the tree)
"""
def get_successor(curr,key):
    while curr.left!=None:
        curr = curr.left
    return curr.data
def delete_in_BST(root,key):
    if root == None:
        return
    if root.data > key:
        root.left = delete_in_BST(root.left,key)
    elif root.data < key:
        root.right = delete_in_BST(root.right,key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            successor = get_successor(root.right,key)
            root.data = successor
            root.right = delete_in_BST(root.right,successor)
    return root

"""
Floor In A BST:
  - Given a value find closest largest smaller or equal value
  - Time complexity: O(h)
  - Auxiliary Space: O(1)
"""
def floor_in_BST(root,key):
    res = None 
    while root!=None:
        if root.data == key:
            return root
        elif root.key > key:
            root = root.left
        else:
            res = root
            root = root.right
    return res

"""
Ceiling In A BST:
    - Given a value find closest smaller greater or equal value
    - Time complexity: O(height of the tree)
    - Auxiliary Space: O(1)

    Algorithmic Conditions:
        - if root's key is same as x, return root
        - if root's key is smaller, then change root to root's right
        - if root's key is greater, update the result as root and change root to root's left
"""
def ceil_in_BST(root,key):
    res = None
    while root!=None:
        if root.key == key:
            return root
        elif root.key<key:
            root = root.right
        else:
            res = root
            root = root.left
    return res

"""
Self-Balancing BST
    - keep height as O(log(n))
    - Same set of keys can make different height BSTs
    - The idea is to do some restructuring (or rebalancing) when doing insertion/deletions
    - We basically do rotation operation and it O(1)
    - Self Balancing BSTs
        = AVL Tree (Strict)
        = Red - Black Tree (Lenient) (easy to restructure)
"""


"""
AVL Tree
    - It is a BST (for every node, left subtree is smaller and right greater)'
    - It is balanced (For every node, difference b/w left and right heights does exceed one)
    - Balance Factor = [left_height - right_height]
    - Balance Factor <= 1
"""
"""
Insert Operation of AVL Tree
    Algorithm:
        - Perform normal BST insert
        - Traverse all ancestor of the newly inserted node from the node to root
        - if find an unbalanced node, check for any of the below cases:
            = Left Left (Single Rotation)
            = Right Right (Single Rotation)
            = Left Right (Double Rotation)
            = Right Left (Double Rotation)
"""

"""
Red - Black Tree
    = Every node is either Red or Black
    = Root is always black
    = No two consecutive Reds
    = Number of black nodes from every node to all of its descendant leaves should be same.
    = Number of nodes on the path from a node to its furthest descendant leaf should not be more than twice than the number of nodes on the path of its closest descendants leaf.
"""
"""
Applications Of BST
    - To maintain sorted stream of data (or sorted set of data)
    - To implement doubly ended priority queue
    - To Solve Problems like:
        = Count smaller/greater in a stream
        = Floor/Ceil/Greater/Smaller in a stream
"""