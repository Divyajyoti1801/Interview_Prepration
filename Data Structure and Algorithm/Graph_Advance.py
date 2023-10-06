from collections import deque
import sys
INT_MAX = 4294967296
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
print()
"""
Connected Components in DFS
"""
def DFS_Utility_2(adj,s,visited):
    visited[s] = True
    print(s,end=" ")
    
    for u in adj[s]:
        if visited[u] == False:
            DFS_Utility_2(adj,u,visited)

def DFS_CC(adj):
    visited = [False]*len(adj)
    res = 0
    for u in range(len(adj)):
        if visited[u] == False:
            res+=1
            DFS_Utility_2(adj,u,visited)
            print()
    return res

adjacent_7 = [[1, 2], [0, 2], [0, 1], [4], [3]]
print_graph(adjacent_7)
print("No. of Connected Components in the graph : ",DFS_CC(adjacent_7))
print()
"""
Application of DFS
    - Cycle Detection
    - Topological Sorting (Dependencies Graph)
    - Strongly Connected Components
    - Solving Maze and Similar Puzzles
    - Path Finding
"""
"""
Shortest Path in an Unweighted Graph
"""
def shortest_path_unweighted_graph(adj,s,dist):
    visited = [False] * len(adj)
    q = deque()
    visited[s] = True
    q.append(s)
    
    while q:
        u = q.popleft()
        
        for v in adj[u]:
            if visited[v] == False:
                dist[v] = dist[u] + 1
                visited[v] = True 
                q.append(v)
adjacent_8 = [[] for i in range(4)]
add_edge_in_graph(adjacent_8,0,1)
add_edge_in_graph(adjacent_8,1,2)
add_edge_in_graph(adjacent_8,2,3)
add_edge_in_graph(adjacent_8,0,2)
add_edge_in_graph(adjacent_8,0,3)
dist_1 = [INT_MAX] * 4
dist_1[0] = 0
shortest_path_unweighted_graph(adjacent_8,0,dist_1)
print("The Shortest Path in a unweighted graph: ",dist_1)
print()

"""
Problem Statement: Detect Cycle in Undirected Graph
"""
def DFS_Utility_3(adj,s,visited,parent):
    visited[s] = True
    for u in adj[s]:
        if visited[u] == False:
            if DFS_Utility_3(adj,u,visited,s):
                return True
            elif u!=parent:
                return True
    return False
def detect_cycle_undirected_graph(adj):
    visited = [False]* len(adj)
    for i in range(len(adj)):
        if visited[i] == False:
            if DFS_Utility_3(adj,i,visited,-1):
                return True
    return False
print("Is there is cycle in an Undirected Graph: ",detect_cycle_undirected_graph(adjacent_8))
print()
"""
Problem Statement : Detect Cycle in a Directed Graph
"""
def add_edge_directed_graph(adj,u,v):
    adj[u].append(v)

def DFS_Utility_4(adj,s,visited,recSt):
    visited[s] = True
    recSt[s] = True

    for u in adj[s]:
        if visited[u] ==False:
            if DFS_Utility_4(adj,u,visited,recSt):
                return True
        elif recSt[u] == True:
            return True
    recSt[s] = False
    return False

def detect_cycle_directed_graph(adj):
    visited = [False]*len(adj)
    recSt = [False] *len(adj)

    for i in range(len(adj)):
        if visited[i] == False:
            if DFS_Utility_4(adj,i,visited,recSt):
                return True
    return False
adjacent_9 = [[] for i in range(4)]
add_edge_directed_graph(adjacent_9,0,1)
add_edge_directed_graph(adjacent_9,1,2)
add_edge_directed_graph(adjacent_9,2,3)
add_edge_directed_graph(adjacent_9,0,2)
add_edge_directed_graph(adjacent_9,0,3)
dist_2 = [INT_MAX] * 4
dist_2[0] = 0
print("Is there is cycle in a directed Graph: ",detect_cycle_directed_graph(adjacent_9))
print()
"""
SORTING ALGO: Topological Sorting
    - Directed Cyclic graph
    BFS based solution (Khan's Algorithm):
        - Store indegree of every vertices
        - Create a Queue, q
        - All all 0 indegree vertices to the q
        - While q is not empty
            - u = q.pop()
            - Print u
            - for every adjacent v of u
                - Reduce indegree of v by 1
                - if indegree of v becomes 0, add v to the q.
        - Time Complexity: O(V+E)
""" 
"""
Implementation of Khan's Algorithm
"""
from collections import defaultdict

class Graph_1:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def topological_sort(self):
        in_degree = [0] * self.V

        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j]+=1
        
        queue = []
        
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)
        cnt = 0
        top_order = []

        while queue:
            u = queue.pop(0)
            top_order.append(u)

            for i in self.graph[u]:
                in_degree[i]-=1
                if in_degree[i] == 0:
                    queue.append(i)
            cnt+=1
        if cnt!=self.V:
            print("There exists a cycle in the graph")
        else:
            print(top_order)
print("Implementation of Khan's Algorithm")
g = Graph_1(6)
g.addEdge(5,2)
g.addEdge(5,0)
g.addEdge(4,0)
g.addEdge(4,1)
g.addEdge(2,3)
g.addEdge(3,1)
print("The Topological Sort of a Given Graph: ")
g.topological_sort()
print()
"""
Topological Sort : Using Depth-First-Search
    Algorithm:
        - Create an Empty stack st
        - For every vertex u, do following
            - if (u is not visited): DFS(u,st)
        - While (st is not empty)
            - pop an item from st and print it
        - Normal DFS
            - Mark U as visited
            - For every adjacent v of u
                - if (v is not visited): DFS(v,st)
            - Push u to st
        - Time Complexity : O(V + E)
"""
class Graph_2:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def topological_sort_DFS_util(self,v,visited,stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_DFS_util(i,visited,stack)
        stack.append(v)
    
    def topological_sort_DFS(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_DFS_util(i,visited,stack)
        print(stack[::-1])
print("DFS Implementation of Topological Sort: ")
g_2 = Graph_2(6)
g_2.addEdge(5,2)
g_2.addEdge(5,0)
g_2.addEdge(4,0)
g_2.addEdge(4,1)
g_2.addEdge(2,3)
g_2.addEdge(3,1)
g_2.topological_sort_DFS()
print()

"""
Shortest Path in Directed Acyclic Graph
    - Initialize Dist[v] = [INF,INF,....,INF]
    - dist[s] = 0
    - Find a topological sort of the graph
    - For every vertex u in the topological sort.
        - For every adjacent v of u
            - if dist[v] > dist[u] + weight(u,v):
                dist[v] = dist[u] + weight(u,v)
"""
class Graph_3:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))
    
    def topological_sort_util(self,v,visited,stack):
        visited[v] = True
        if v is self.graph.keys():
            for node,weight in self.graph[v]:
                if visited[node] == False:
                    self.topological_sort_util(node,visited,stack)
        stack.append(v)
    
    def shortest_path(self,s):
        visited = [False]*self.V
        stack = []
        
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(s,visited,stack)
        dist = [float("Inf")] * self.V
        dist[s] = 0
        
        while stack:
            i = stack.pop()
            for node,weight in self.graph[i]:
                if dist[node]>dist[i] + weight:
                    dist[node] = dist[i] + weight
        
        for i in range(self.V):
            print (("%d" %dist[i]) if dist[i] != float("Inf") else "Inf" ,end=" ")

g_3 = Graph_3(6)
g_3.addEdge(0,1,5)
g_3.addEdge(0,2,3)
g_3.addEdge(1,3,6)
g_3.addEdge(1,2,2)
g_3.addEdge(2,4,4)
g_3.addEdge(2,5,2)
g_3.addEdge(2,3,7)
g_3.addEdge(3,4,-1)
g_3.addEdge(4,5,-2)
print("Shortest Path acyclic directed Graph: ")
g_3.shortest_path(1)
print()

"""
Minimum Spanning Tree
    - Tree Structure: Weighted and Connected Undirected Graph
    - For Example:
        :: Minimize the wire length and make sure that all computer's are connected to each other may be through intermediate computer.
    - What is a Spanning Tree:
        :: A tree which is connected by doesn't have any cycle
            - V edges, but we want (V - 1) edges

Prim's Algorithm (Cut-Edge Theory)
    - It has two Sets
        = In MST
        = Not Yet in MST
    - We go for edge which has minimum weight
    
    Ideas for Better Implementation: 
        - The normal implementation time complexity O(V^2)
        - Use Adjacency List representation
        - Use min heap
        - With this changes time complexity will become O((E + V) * log(V))
"""
class Graph_4:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    
    def print_minimum_spanning_tree(self,parent):
        print("Edge \t Wight")
        for i in range(1,self.V):
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
    
    def min_key(self,key,mstSet):
        min = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v]<min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index
    
    def primary_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1 # type: ignore
        
        for count in range(self.V):
            u = self.min_key(key,mstSet)
            mstSet[u] = True
            
            for v in range(self.V):
                if self.graph[u][v]>0 and mstSet[v] == False and key[v]>self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u # type: ignore
        self.print_minimum_spanning_tree(parent)
g_4 = Graph_4(5)
g_4.graph = [[0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]
g_4.primary_mst()
print()

"""
Dijkstra's Shortest Path Algorithm
    :: Given a weighted graph and a source, find shortest distances from sources to all other vertices.

Interesting Facts/Questions:
    - Does not work for negative weight edges
    - Does the shortest path change if add a weight to all edges of the original Path

Algorithm:
    - Create an empty Priority Queue (or Min Heap),pq
    - dist[v] = {inf,inf,....,inf}
    - dist[s] = 0
    - Insert all distance into pq
    - While pq.empty() == false; u = pq.extractMin(); Relax all adjacent of u that are not in pq

Ideas for better implementation
    - Use Adjacency list representation
    - Use Min-Heap
    - With above optimization we get Time Complexity O((V+E)*log(V))
"""
def dijkstra(graph,src):
    V = len(graph)
    dist = [float('inf') for i in range(V)]
    dist[src] = 0
    fin = [False for i in range(V)]

    for count in range(V-1):
        u = -1
        for i in range(V):
            if fin[i] == False and (u==-1 or dist[i]<dist[u]):
                u = i
        fin[u] = True
            
        for x in range(V):
            if fin[x] == False and graph[u][x]!=0:
                dist[x] = min(dist[x],dist[u]+graph[u][x])
    return dist
graph_1 = [[0,5,10,0],[5,0,3,20],[10,3,0,2],[0,20,2,0]]
print("The Shortest Path Algorithm (Dijkstra Algorithm): ",dijkstra(graph_1,0))
print()

"""
Kosaraju's Algorithm (Strongly Connected Component Graphs)
    - Printing all strongly connected components 

Algorithm:
    - Order the vertices in decreasing order of finish times in DFS
    - Reverse all edges
    - Do DFS of the reversed graph in the order obtained in Step-1. For every vertex print all reachable vertices as one strongly connected.

Pseudo Code Step-1:
    - Create an empty stack, st
    - For every vertex u, do the following:
        = if (u is not visited): DFSRec(u,st)
    - While (st is not empty)
        = Pop an item and add to result
    - DFSRec(u,st)
        = Mark u as visited
        = For every adjacent v; if(v is not visited) DFSRec(v,st)
        = st.push(u)
Time Complexity: O(V+E)
"""
"""
Bellman Ford Algorithm : Shortest Path Algorithm
    - We first find shortest paths that are of one edge length. Then shortest paths that are of two edge length and so on.
Algorithm : We relax all edges V-1 times
"""
class Graph_5:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []
    
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def print_array(self,dist):
        print("Vertex Distance from Source: ")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i,dist[i]))
    
    def bellmanFord(self,src):
        dist = [float("Inf")]*self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for u,v,w in self.graph:
                if dist[u]!= float("Inf") and dist[u]+w<dist[v]:
                    dist[v] = dist[u] + w
        
        for u,v,w in self.graph:
            if dist[u]!= float("Inf") and dist[u]+w<dist[v]:
                print("Graph contains negative weight cycle")
                return 
        self.print_array(dist)
print("Shortest Path Algorithm: ")
g_5 = Graph_5(5)
g_5.addEdge(0,1,-1)
g_5.addEdge(0,2,4)
g_5.addEdge(1,2,3)
g_5.addEdge(1,3,2)
g_5.addEdge(1,4,2)
g_5.addEdge(3,2,5)
g_5.addEdge(3,1,1)
g_5.addEdge(4,3,-3)
g_5.bellmanFord(0)