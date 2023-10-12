"""
GRAPH DATA STRUCTURE
"""
# Libraries we are going to use
from collections import deque

"""
Types of Graphs

- Directed Graph (Only one-way & Pairs are ordered)
    = In-Degree (No. of Edges Incoming) 
    = Out-Degree (No. of Edges Outgoing)
    = Sum of In-Degree : |E| 
    = Sum of Out-Degree : |E|
    = Maximum number of Edges : |V| * (|V| - 1)

- Un-Directed Graph (Both-ways & Pairs are un-ordered)
    = Sum of Degree = 2 * |E|
    = Maximum number of Edges = [ |V| * (|V| - 1) ]/2

- Weighted Graph : City road network

- Un-Weighted Graph
"""

"""
Some Generalized Terms
    - Walk : (Repetition of vertices happen) (Path)
    - Path : (Repetition of vertices doesn't happen) (Simple Path)
    
    - Cyclic Graph : There exists a walk that begins and ends with same vertex
    - Acyclic Graph : There exists a walk that begins and ends with different vertices
        = Undirected Acyclic Graph
        = Directed Cyclic Graph (DAG)
"""

"""
Graph Representation in Programming
    
    - Adjacency Matrix
        = Size of matrix = |V| * |V|; |V| = Number of vertices
        = For Undirected Graph : It is a symmetric matrix.
        = mat[i][j] = { 1 : If there is an edge from vertex j; 0 : otherwise}

        How to handle vertices with arbitrary names?
            - For efficient implementation, one hash table h would also be required to do reverse mapping.
        
        Properties of Adjacency Matrix Representation:
            - Space Required : theta(V * V)
            - Operations:
                = Check if u and v are adjacent : theta(1)
                = Find all vertices adjacent to u : theta(V)
                = Find degree of u : theta(V)
                = Add/Remove an Edge : theta(1)
                = Add/Remove a Vertex : theta(V)
    
    - Adjacency List
        = Array of list stores the connected vertices.
        = Popularly represented as :
            - Dynamic Sized Arrays (Mostly used due to cache friendliness)
            - Linked Lists
        
        Properties of Adjacency List Representation:
            - Space Required : theta(V + E)
                = Undirected Graph : theta(V + (2*E))
                = Directed Graph : theta(V + E)
"""
"""
Implementation of Graph Representation through Adjacency List (Linked List)
"""
class adjacency_node:
    def __init__(self,data):
        self.vertex = data
        self.next = None
class Graph_Adjacency:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [None] * self.V
    
    def add_edge(self,src,dest):
        node = adjacency_node(dest)
        node.next= self.graph[src]
        self.graph[src] = node # type: ignore
        
        node = adjacency_node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node # type: ignore
    
    def print_graph(self):
        for i in range(self.V):
            print("adjacency list of vertex {}: Head".format(i),end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex),end=" ")
                temp = temp.next
            print()

print("Graph representation through Adjacency List(Linked List) : ")
graph_adjacency_1 = Graph_Adjacency(5)
graph_adjacency_1.add_edge(0,1)
graph_adjacency_1.add_edge(0,4)
graph_adjacency_1.add_edge(1,2)
graph_adjacency_1.add_edge(1,3)
graph_adjacency_1.add_edge(1,4)
graph_adjacency_1.add_edge(2,3)
graph_adjacency_1.add_edge(3,4)
graph_adjacency_1.print_graph()
print()
"""
Implementation of Graph Representation through Adjacency List (Dynamic List)
"""
def add_edge_list(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def print_dynamic_list(adj):
    for u,l in enumerate(adj):
        print(u,l)
print("Graph representation through Adjacency List(Dynamic List) : ")
graph_Adjacency_2 = [[] for i in range(4)]
add_edge_list(graph_Adjacency_2,0,1)
add_edge_list(graph_Adjacency_2,0,2)
add_edge_list(graph_Adjacency_2,1,2)
add_edge_list(graph_Adjacency_2,1,3)
print(graph_Adjacency_2)
print()

"""
Comparison of Adjacency list and Adjacency Matrix

    - Undirected : 0 <=E <=(V * (V - 1))/2
    - Directed : 0 <= E <= (V * (V - 1))

=> There is a takeaway the graph which have vertices less then the upper mentioned range is called "SPARSE GRAPH". More than the upper mentioned range is called "DENSE GRAPH"

Adjacency List Time Complexity for different operations:
    - Memory : theta(V + E)
    - Check if there is an edge from u to v : O(V)
    - Find all adjacent of u : theta(degree(U))
    - Add an Edge : theta(1)
    - Remove an Edge : O(V)

Adjacency Matrix Time Complexity for different operations:
    - Memory : theta(V + V)
    - Check if there is an edge from u to v : theta(1)
    - Find all adjacent of u : theta(V)
    - Add an Edge : theta(1)
    - Remove an Edge : O(1)
"""

"""
Breadth-First-Search : Graph Traversal Algorithm
    - Given an undirected graph and a source vertex 's' print BFS from the given source.
"""
def Add_Edge_1(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def print_graph(adj):
    for u,l in enumerate(adj):
        print(u,l)

def Breadth_First_Search(adj,s):
    visited = [False] * len(adj)
    q = deque()
    q.append(s)
    visited[s] = True
    
    while q:
        s = q.popleft()
        print(s , end = " ")

        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True

print("Adjacent list Graph: ")
adjacent_1 = [[1,2],[0,2,3],[0,1,3,4],[1,2,4],[2,3]]
print_graph(adjacent_1)
print("Breadth First Search (First Version): ")
Breadth_First_Search(adjacent_1,0)
print("\n")

"""
Breadth-First-Search of Disjoint Graph
    - Time Complexity : O(V + E)
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

def BFS_disjoint(adj):
    visited  = [False] * len(adj)
    for u in range(len(adj)):
        if visited[u] == False:
            BFS_utility_1(adj,u,visited)

adjacent_2_disjoint=[[1,2],[0,3],[0,3],[1,2],[5,6],[4,6],[4,5]]
print("Adjacent List of a Disjoint Graph: ")
print_graph(adjacent_2_disjoint)
print("Breadth First Search (Disjoint Graph): ")
BFS_disjoint(adjacent_2_disjoint)
print("\n")

"""
Breadth-First-Search of a connected components of a Undirected Graph
"""
def BFS_utility_2(adj,s,visited):
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        s = q.popleft()
        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True
def connected_components(adj):
    visited = [False] * len(adj)
    res = 0
    for u in range(len(adj)):
        if visited[u] == False:
            res+=1
            BFS_utility_2(adj,u,visited)
    return res
adjacent_3_disjoint= [[1,2],[0,2],[0,1],[4],[3],[6,7],[5],[5]]
print("Adjacent List of a Disjoint Graph: ")
print_graph(adjacent_3_disjoint)
print("No. of Connected Components of Graph: ",connected_components(adjacent_3_disjoint))
print()

"""
Application of Breadth-First-Search
    - Shortest Path in an unweighted graph
    - Crawlers in Search-Engines
    - Peer to Peer Networks
    - Social Networking Search
    - In Garbage-Collection (Cheney's Algorithm)
    - Cycle Detection
    - Ford Fulkerson Algorithm
    - Broadcasting
"""

"""
Depth-First-Search for Un-Directed Connected Graph
    - We will pick lowest valued vertex as source to start DFS traversal
"""
def DFS_utility(adj,s,visited):
    visited[s] = True
    print(s,end=" ")
    for u in adj[s]:
        if visited[u] == False:
            DFS_utility(adj,u,visited)
def Depth_First_Search(adj,s):
    visited = [False] * len(adj)
    DFS_utility(adj,s,visited)
print("Adjacent List of Undirected Connected Graph: ")
adjacent_4 = [[1,2],[0,3,4],[0,3],[1,2,4],[1,3]]
print_graph(adjacent_4)
print("Depth First Search of an undirected connected graph: ")
Depth_First_Search(adjacent_4,0)
print("\n")