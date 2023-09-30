from collections import deque
"""
GRAPH DATA STRUCTURE : Non-Linear Data Structure

    Directed Graph: 
        - InDegree (V3) = 1
        - OutDegree (v3) = 2
        - Sum of InDegree  = |E|
        - Sum of OutDegree = |E|
        - Maximum number of edges = |V| * (|V|-1)
    
    Undirected Graph:
        - Degree(V3) = 3
        - Sum Of Degree = 2 * |E|
    
    V1 --> V2 --> v4
    Walk: V1, V2, V4, V2 (Path)
    Path: V1, V2, V4 (Simple Path)
    Cyclic: There exists a walk that begins and same with same vertex

    Cyclic: Cyclic Undirected, Cyclic Directed
    Acyclic:  Undirected Acyclic Graph, Directed Acyclic Graph
    
    Weighted & UnWeighted Graph
"""
"""
Adjacency Matrix
    - Size of matrix : |V| * |V|; |V| = Number of vertices.
    - For Undirected Graph: It is a symmetric matrix
    - mat[i][j] = {1 : If there is an edge from vertex i to vertex j; 0 : Otherwise}

Properties of Adjacency Matrix Representation:
    - Space Required: O(v*v)
    - Operations:
        = Check if u and v are adjacent: O(1)
        = Find all vertices adjacent to u: O(v)
        = Find degree of u : O(v)
        = Add/Remove and Edge : O(1)
        = Add/Remove a vertex : O(v^2)
Problem:
    - Stores redundant information
"""
"""
Adjacent List
    - An Array of lists where
    - List are most popularly represented as:
        = Dynamic Sized Arrays
        = Linked Lists
    - Auxiliary Space Complexity: O(V + E),
        = Undirected Graph: V + (2*E)
        = Directed Graph: V + E
    - Operations:
        = Check if there is an Edge from U to V: O(V)
        = Find All adjacent of u: O(degree(U))
        = Find degree of u: O(1)
        = Add an Edge: O(1)
        = Remove an Edge: O(V)
"""

"""
Graph Adjacency List Representation
"""
def add_edge_in_graph(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def print_graph(adj):
    for u,l in enumerate(adj):
        print(u,l)

vertices_1 = 4
adjacent_1  = [[] for i in range(vertices_1)]
add_edge_in_graph(adjacent_1,0,1)
add_edge_in_graph(adjacent_1,0,2)
add_edge_in_graph(adjacent_1,1,2)
add_edge_in_graph(adjacent_1,1,3)
print("Graph Adjacency List Representation: ",adjacent_1)
print()
"""
Breadth-First-Search(BFS)
    - Version_1: Given an undirected graph and a source vertex "s" print BFS from the given source
"""
def BFS_1(adj,s):
    visited = [False] * len(adj)
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        s = q.popleft()
        print(s,end = " ")
        
        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True
    print()
print("Breadth First Search (Version-1): ")
adjacent_2  = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4], [2, 3]]
print_graph(adjacent_2)
print("BFS Path: ")
BFS_1(adjacent_2,0)
print()