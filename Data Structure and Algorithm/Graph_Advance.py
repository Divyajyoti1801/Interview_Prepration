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

"""
- Version_2: BFS for Disconnected Graph
"""
def BFS_utility_1(adj,s,visited):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        s = q.popleft()
        print(s,end=" ")

        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True
    print()

def BFS_disjoint(adj):
    visited = [False] * len(adj)
    for u in range(len(adj)):
        if visited[u] == False:
            BFS_utility_1(adj,u,visited)

adjacent_3 = [[1, 2], [0, 3], [0, 3], [1, 2], [5, 6], [4, 6], [4, 5]]
print_graph(adjacent_3)
print("BFS Path of Disjoint Graph: ")
BFS_disjoint(adjacent_3)

"""
Connected Components in an Undirected Graph
"""
def BFS_utility_2(adj,s,visited):
    q = deque()
    q.append(s)
    visited[s]=True

    while q:
        s = q.popleft()
        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True
    print()

def BFS_disjoint_CC(adj):
    visited = [False] * len(adj)
    res = 0
    for u in range(len(adj)):
        if visited[u] == False:
            res += 1
            BFS_utility_2(adj,u,visited)
    return res
adjacent_4 = [[1, 2], [0, 2], [0, 1], [4], [3], [6,7], [5],[5]]
print("Connected Component of a disjoint graph: ",BFS_disjoint_CC(adjacent_4))
print()

"""
Application BFS
    - Shortest path in an unweighted graph
    - Web-Crawlers in Search Engine
    - Peer-to-Peer Network
    - Social Networking Search
    - In Garbage Collection (Cheney's Algorithm)
    - Cycle Detection
    - Ford Fulkerson Algorithm
    - Broadcasting Algorithm 
"""

"""
Depth First Search (DFS) : Recursive in Nature
Version_1: Choosing Min Value vertex as a starting point
"""
def DFS_Utility_1(adj,s,visited):
    visited[s] = True
    print(s,end=" ")
    for u in adj[s]:
        if visited[u] == False:
            DFS_Utility_1(adj,u,visited)

def DFS(adj,s):
    visited = [False] * len(adj)
    DFS_Utility_1(adj,s,visited)

adjacent_5 = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3]]
print_graph(adjacent_5)
print("Depth Fist Search Path:")
DFS(adjacent_5,0)
print()
print()
"""
Version 2: DFS of a Disjoint Graph
"""
def DFS_disjoint(adj):
    visited = [False]*len(adj)
    for u in range(len(adj)):
        if visited[u] == False:
            DFS_Utility_1(adj,u,visited)
adjacent_6 = [[1, 2], [0, 2], [0, 1], [4], [3]]
print_graph(adjacent_6)
print("DFS of a Disconnected Graph: ")
DFS_disjoint(adjacent_6)