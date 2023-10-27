"""
DISJOINT SOLUTION
"""

"""
Example Problem : n = 4
    - make_friends(0,1) ; make_friends(1,3) ; are_friends(0,2) ; are_friends(0,3)
    - I/P :[0] , [1] , [2] , [3] 
        = make_friends(0,1) : [0,1] , [2] , [3]
        = make_friends(0,3) : [0,1,3] , [2]
        = are_friends(0,2) : No
        = are_friends(0,1) : Yes
        = are_friends(0,3) : Yes

Simple Solution for Disjoint Set :
    - Use Adjacency List or Adjacency Matrix Representation
    - Adjacency List : make_friends() and are_friends() are O(n)
    - Adjacency Matrix : make_friends() is theta(n) and are_friends is theta(1)

Better Solution of Disjoint Set :
    - find(x) : Returns a representative of x's set (or Social Network)
    - union(x,y) : Combine sets of x and y (same as make_friends())
    - boolean are_friends(x,y) return find(x) == find(y)
    - make_friends(x,y) : union(x,y)
"""
DISJOINT_PARENT = [i for i in range(5)]
DISJOINT_RANK = [0 for i in range(5)]

def find(x):
    if DISJOINT_PARENT[x] == x:
        return x
    return find(DISJOINT_PARENT[x])

def union(x,y):
    x_rep = find(x)
    y_rep = find(y)
    if(x_rep == y_rep):
        return
    DISJOINT_PARENT[y_rep] = x_rep

""""
Union By Rank
    - We use an extra array, rank in the union operation
    - It typically stores heights
    - The idea is to make representative of smaller height as child of the other one
"""
def union_by_rank(x,y):
    x_rep = find(x)
    y_rep = find(y)
    if x_rep == y_rep:
        return 
    if DISJOINT_RANK[x_rep] < DISJOINT_RANK[y_rep]:
        DISJOINT_PARENT[x_rep] = y_rep
    elif DISJOINT_RANK[x_rep] > DISJOINT_RANK[y_rep]:
        DISJOINT_PARENT[y_rep] = x_rep
    else:
        DISJOINT_PARENT[y_rep] = x_rep
        DISJOINT_RANK[x_rep] += 1
    return (DISJOINT_PARENT,DISJOINT_RANK)
print("Union By Rank : ",union_by_rank(3,4))
print()

"""
Path Compression
    - The idea is to modify and optimize the tree in the find()
Idea: 
    - We make parent of all nodes(on the path from given node to root) as root
"""

def find_path_compression(x):
    if DISJOINT_PARENT[x] == x:
        return x
    DISJOINT_PARENT[x]=find(DISJOINT_PARENT[x])
    return DISJOINT_PARENT[x]