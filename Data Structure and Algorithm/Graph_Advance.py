"""
GRAPH DATA STRUCTURE
"""
# Libraries we are going to use
from collections import deque,defaultdict
import sys
INT_MAX = 4294967296
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

def Add_Edge_2(adj,u,v):
    adj[u].append(v)


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
def DFS_utility_1(adj,s,visited):
    visited[s] = True
    print(s,end=" ")
    for u in adj[s]:
        if visited[u] == False:
            DFS_utility_1(adj,u,visited)
def Depth_First_Search(adj,s):
    visited = [False] * len(adj)
    DFS_utility_1(adj,s,visited)
print("Adjacent List of Undirected Connected Graph: ")
adjacent_4 = [[1,2],[0,3,4],[0,3],[1,2,4],[1,3]]
print_graph(adjacent_4)
print("Depth First Search of an undirected connected graph: ")
Depth_First_Search(adjacent_4,0)
print("\n")

"""
Depth-First-Search for counting connected components in an Un-Directed Graph
"""
def DFS_utility_2(adj,s,visited):
    visited[s] = True
    for u in adj[s]:
        if visited[u] == False:
            DFS_utility_2(adj,u,visited)
    
def connected_components_DFS(adj):
    visited = [False] * len(adj)
    res = 0
    for u in range(len(adj)):
        if visited[u] == False:
            res+=1
            DFS_utility_2(adj,u,visited)
    return res
adjacent_5 = [[1,2],[0,2],[0,1],[4],[3]]
print("Un-Directed Graph: ")
print_graph(adjacent_5)
print("No. of Connected Components in an Un-Directed Graph (DFS): ",connected_components_DFS(adjacent_5))
print()

"""
Application of Depth-First-Search
    - Cycle Detection
    - Topological Sorting
    - Strongly Connected Components
    - Solving Maze and similar Puzzles
    - Path Finding
"""

"""
Shortest Path in Un-Weighted Graph
"""
def shortest_path_unWeighted(adj,s,dist):
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

adjacent_6 = [[] for i in range(4)]
add_edge_list(adjacent_6,0,1)
add_edge_list(adjacent_6,1,2)
add_edge_list(adjacent_6,2,3)
add_edge_list(adjacent_6,0,2)
add_edge_list(adjacent_6,0,3)
print("Un-Weighted Graph: ")
print_graph(adjacent_6)
dist_SPW = [INT_MAX]*4
dist_SPW[0] = 0
shortest_path_unWeighted(adjacent_6,0,dist_SPW)
print("Shortest Path in Un-Weighted Graph: ",dist_SPW)
print()

"""
Detect Cycle in Un-Directed Graph
"""
def DFS_utility_3(adj,s,visited,parent):
    visited[s] =True
    for u in adj[s]:
        if visited[u]== False:
            if DFS_utility_3(adj,u,visited,s):
                return True
            elif u!=parent:
                return True
    return False

def detect_cycle_unDirected(adj):
    visited = [False] * len(adj)
    for i in range(len(adj)):
        if(visited[i] == False):
            if DFS_utility_3(adj,i,visited,-1):
                return True
    return False

adjacent_7 = [[] for i in range(4)]
add_edge_list(adjacent_7,0,1)
add_edge_list(adjacent_7,1,2)
add_edge_list(adjacent_7,2,3)
add_edge_list(adjacent_7,0,2)
add_edge_list(adjacent_7,0,3)
print("Cycle Detection Graph: ")
print_graph(adjacent_7)
print("Is Graph is Cyclic (joint & disjoint) Undirected: ",detect_cycle_unDirected(adjacent_7))
print()

"""
Detect Cycle in a Directed Graph
"""
def DFS_utility_4(adj,s,visited,rec_stack):
    visited[s] = True
    rec_stack[s] = True

    for u in adj[s]:
        if visited[u] == False:
            if DFS_utility_4(adj,u,visited,rec_stack):
                return True
            elif rec_stack[u] == True:
                return True
    rec_stack[s] = False
    return False

def detect_cycle_directed(adj):
    visited = [False] * len(adj)
    rec_stack = [False] * len(adj)

    for i in range(len(adj)):
        if (visited[i] == False):
            if DFS_utility_4(adj,i,visited,rec_stack):
                return True
    return False

adjacent_8 = [[] for i in range(4)]
add_edge_list(adjacent_8,0,1)
add_edge_list(adjacent_8,1,2)
add_edge_list(adjacent_8,2,3)
add_edge_list(adjacent_8,0,2)
add_edge_list(adjacent_8,0,3)
print("Directed Graph for Cycle Detection: ")
print_graph(adjacent_8)
print("Is Cycle present in Directed Graph: ",detect_cycle_directed(adjacent_8))
print()

"""
Topological Sorting (Kahn's BFS Based Algorithm)
"""
class Graph_kahn:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def topologicalSort(self):
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
        if cnt!= self.V:
            print("There exists a cycle in the Graph")
        else:
            print(top_order)
g_1 = Graph_kahn(6)
g_1.addEdge(5,2)
g_1.addEdge(5,0)
g_1.addEdge(4,0)
g_1.addEdge(4,1)
g_1.addEdge(2,3)
g_1.addEdge(3,1)
print("Topological Sort (Kahn's BFS Algorithm): ")
g_1.topologicalSort()
print()

"""
Cycle Detection with Kahn's Algorithm (BFS)
    - Using a Directed Graph
"""
def cycle_detection_2(adj):
    V = len(adj)
    in_degree = [0]*V
    
    for u in range(V):
        for x in adj[u]:
            in_degree[x]+=1
    
    q = deque()

    for i in range(V):
        if in_degree[i] == 0:
            q.append(i)
    count = 0

    while q:
        u = q.popleft()

        for x in adj[u]:
            in_degree[x] -=1
            if in_degree[x] == 0:
                q.append(x)
        count +=1
    
    if count != V:
        print("There exists a cycle in the graph")
    else:
        print("There exists no cycle in the graph")
adjacent_9 = [[] for i in range(4)]
Add_Edge_2(adjacent_9,0,1)
Add_Edge_2(adjacent_9,1,2)
Add_Edge_2(adjacent_9,2,3)
Add_Edge_2(adjacent_9,0,2)
Add_Edge_2(adjacent_9,0,3)
print("Connected Graph for Cycle Detection: ")
print_graph(adjacent_9)
print("Is Cycle present in the graph: ")
cycle_detection_2(adjacent_9)
print()

"""
Topological Sort using Depth-First-Search

Pseudo Code:
    - Create an Empty stack st
    - For every vertex u, do following
        = if (u is not visited): DFS(u,st)
    - While (st is not empty)
        = Pop an item from st and print it.
    - DFS(u,st)
        = Mark u as visited
        = For every adjacent v of u
            - if (v is not visited): DFS(v,st)
        = Push u to st
"""
class Graph_topological_DFS:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def topological_sort_util(self,v,visited,stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i,visited,stack)
        stack.append(v)
    
    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i,visited,stack)
        print(stack[::-1])

graph_Adjacency_3 =Graph_topological_DFS(6)
graph_Adjacency_3.addEdge(5,2)
graph_Adjacency_3.addEdge(5,0)
graph_Adjacency_3.addEdge(4,0)
graph_Adjacency_3.addEdge(4,1)
graph_Adjacency_3.addEdge(2,3)
graph_Adjacency_3.addEdge(3,1)
print("Graph for Topological Sort DFS: ")
graph_Adjacency_3.topological_sort()
print()

"""
Shortest Path in a Directed_Acyclic_Graph

Pseudo Code:
    shortest_path(adj,s)
        - Initialize dist[v] = {INF,INF,...,INF}
        - dist[s] = 0
        - Find a topological sort of the graph
        - For every vertex u in the topological sort.
            = For every adjacent v of u.
                - if dist[v] > dist[u] + weight(u,v)
                    dist[v] = dist[u] + weight(u,v)
"""
class Graph_DAG:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self,u,v,w):
        self.graph[u].append((v,w))
    
    def topological_sort_util(self,v,visited,stack):
        visited[v] = True
        
        if v in self.graph.keys():
            for node,weight in self.graph[v]:
                if visited[node] == False:
                    self.topological_sort_util(node,visited,stack)
        stack.append(v)

    def shortest_path(self,s):
        visited=[False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(s,visited,stack)
        dist = [float("Inf")] * self.V
        dist[s] = 0

        while stack:
            i = stack.pop()
            for node,weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight
        for i in range(self.V):
            print("%d"%dist[i] if dist[i]!= float("Inf")else "Inf", end = " ")
graph_dag = Graph_DAG(6)
graph_dag.add_edge(0,1,5)
graph_dag.add_edge(0,2,3)
graph_dag.add_edge(1,3,6)
graph_dag.add_edge(1,2,2)
graph_dag.add_edge(2,4,4)
graph_dag.add_edge(2,5,2)
graph_dag.add_edge(2,3,7)
graph_dag.add_edge(3,4,-1)
graph_dag.add_edge(4,5,-2)
print("Shortest distance from source 1: ")
graph_dag.shortest_path(1)
print("\n")
"""
Minimum Spanning Tree : Prim's Algorithm
    - Case Study: Minimize the wire length and make sure that all computers are connected to each other may be through intermediate computers

    - Given a weighted, undirected and connected graph, find minimum spanning tree of it.
    - SPANNING TREE : A tree there should not be in cycle and connect each vertices.

Better Implementation
    - Use adjacency list representation
    - Use Min-Heap
    - With this optimization we get time as O((E+V)* log(V)) which can be written as O(E log(V)) for a connected graph   
"""
class Graph_Prims:
    def __init__(self,vertices):
        self.V = vertices
        self.graph=[[0 for column in range(vertices)] for row in range(vertices)]
    
    def print_MST(self,parent):
        print("Edge \tWeight")
        for i in range(1,self.V):
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
    
    def min_key(self,key,mstSet):
        min = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index
    
    def prims_algo(self):
        key = [sys.maxsize] *self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set= [False] * self.V
        parent[0] = -1 # type: ignore

        for count in range(self.V):
            u = self.min_key(key,mst_set)
            mst_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mst_set[v] == False and key[v]>self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u # type: ignore
        self.print_MST(parent)

graph_adjacency_4 = Graph_Prims(5)
graph_adjacency_4.graph = [[0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]
graph_adjacency_4.prims_algo()
print()

"""
Dijkstra's Algorithm
    - Given a weighted graph and a source find shortest distance from source to all other vertices.
    - Doesn't work for negative weight edge
    - Does the shortest path changes if add a weight to all edges of the original graph. -- YES

Pseudo Code:
    - Create empty Priority Queue (or Min-Heap), pq
    - dist[v] = {Inf,Inf,Inf.......}
    - dist[s] = 0
    - Insert all distance into pq
    - While pq.empty() == false
        {
            u = pq.extractMin() --> O(log(V))
            Relax all adjacent of u that are not in pq --> O(log(V))
        }
"""
def dijkstra_algo(graph,src):
    V = len(graph)
    dist = [float("inf") for i in range(V)]
    dist[src] = 0
    fin = [False for i in range(V)]
    
    for count in range(V-1):
        u = -1
        for i in range(V):
            if fin[i] == False and (u == -1 or dist[i]<dist[u]):
                u = i
        fin[u] = True
        for x in range(V):
            if(fin[x]== False and graph[u][x]!=0):
                dist[x] = min(dist[x],dist[u]+graph[u][x])
    return dist
graph_adjacency_5 = [[0,5,10,0],[5,0,3,20],[10,3,0,2],[0,20,2,0]]
print("Dijkstra's Algo Source to all other vertices to shortest path distance: ",dijkstra_algo(graph_adjacency_5,0))
print()

"""
Kosaraju's Algorithm of Strongly Connected Components
    - Based on Depth-First-Search
    - Traverse Direction : Sync Compo to Starting Compo
Algorithm Steps:
    Step 1 : Order the vertices in decreasing order of finish times in DFS
    Step 2 : Reverse all edges
    Step 3 : Do DFS of the reversed graph in the order obtained in Step 1. For every vertex, print all reachable vertices as one Strongly Connected Component.

    Implementation of Step-1:
        - Create an empty stack,st
        - For every vertex u, do the following:
            - if u is not visited: DFS_utility(u,st)
        - While(st is not empty)
            - pop an item and add to result
        - DFSRec(u,st)
            = Mark u as visited
            = For every adjacent v
                - if v is not visited: DFS_utility(v,st)
            = st.push(u)
"""
class Graph_Kosaraju:
    def DFS(self,curr,des,adj,vis):
        if curr == des:
            return True
        vis[curr] = 1
        for x in adj[curr]:
            if not vis[x]:
                if self.DFS(x,des,adj,vis):
                    return True
        return False
    
    def is_path(self,src,des,adj):
        vis = [0] * (len(adj) + 1)
        return self.DFS(src,des,adj,vis)
    
    def strongly_connected_component(self,n,a):
        ans = []
        
        is_scc = [0]*(n+1)

        adj = [[] for _ in range(n+1)]
        
        for i in range(len(a)):
            adj[a[i][0]].append(a[i][1])
        
        for i in range(1,n+1):
            if not is_scc[i]:
                scc = [i]
                for j in range(i+1,n+1):
                    if not is_scc[j] and self.is_path(i,j,adj) and self.is_path(j,i,adj):
                        is_scc[j] = 1
                        scc.append(j)
                ans.append(scc)
        return ans

graph_kosaraju = Graph_Kosaraju()
graph_kosaraju_edges= [[1,3],[1,4],[2,1],[3,2],[4,5]]
print("Kosaraju's Algorithm (Find Strongly Connected Components): ",graph_kosaraju.strongly_connected_component(5,graph_kosaraju_edges))
print()
"""
Bellman Ford Algorithm : Dynamic Programming Algorithm
    - Counters downside of Dijkstra's Algorithm of negative weights.
    - Solve the same problem shortest path from source to all vertices.
Idea:
    - We first find shortest paths that are of one edge length. Then shortest paths that are of two edge length and so on.
Algorithm: We relax all edges V-1 times
    - d[v] = {Inf,Inf,......Inf}
    - d[s] = 0
    - for (count = 0; count < (V-1); count++):
        = if(d[v] > d[u] + weight(u,v)):
            d[v] = d[u] + weight(u,v)
    - for every edge(u,v):
        = if(d[v] > d[u] + weight(u,v)):
            print("Negative weight cycle found")

Time Complexity : O(V*E)
"""
class Graph_BellmanFord:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []
    
    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def print_array(self,dist):
        print("Vertex distance from source: ")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i,dist[i]))
    
    def bellmanFord_algo(self,src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        
        for _ in range(self.V - 1):
            for u,v,w, in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        for u,v,w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph Contains negative weight Cycle")
                return
        self.print_array(dist)
print("Bellman Ford Algorithm")
graph_bellmanford = Graph_BellmanFord(5)
graph_bellmanford.add_edge(0,1,-1)
graph_bellmanford.add_edge(0,2,4)
graph_bellmanford.add_edge(1,2,3)
graph_bellmanford.add_edge(1,3,2)
graph_bellmanford.add_edge(1,4,2)
graph_bellmanford.add_edge(3,2,5)
graph_bellmanford.add_edge(3,1,1)
graph_bellmanford.add_edge(4,3,-3)
graph_bellmanford.bellmanFord_algo(0)
print()
"""
Articulation Point
    - Undirected & Connected Graph
    - A point with its removal it created more connected components is called Articulation Point

Efficient First Idea : 
    - If root of DFS Tree has 2 or more children, then the root is an articulation point.
    - Time Complexity : O(V * (V+E))
    - This idea can only be used for root of DFS Tree

Efficient Second Idea :
    - If a non-root node u in DFS Tree has a child v such that no ancestors are reachable from the subtree rooted with v, then u is an articulation point.

Implementation Details:
    - discovery[u] : Time at which DFS for u is called
    - low[u] : Lowest discovery time reachable from u considering both types of edges
    - A non-root node u is an articulation point if there exist a child v such that low[v]>=discovery[u]

    Node : 0 1 2 3 4 5 6
    Disc : 1 2 3 4 5 6 7
    Low  : 1 1 1 1 5 5 5
"""
class Graph_Articulation:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def articulation_point_util(self,u,visited,ap,parent,low,disc):
        children = 0
        visited[u] = True
        
        disc[u] = self.Time
        low[u] = self.Time

        self.Time +=1

        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                children += 1
                self.articulation_point_util(v,visited,ap,parent,low,disc)
                low[u] = min(low[u],low[v])

                if parent[u]==-1 and children>1:
                    ap[u] = True
                
                if parent[u]!= -1 and low[v]>=disc[u]:
                    ap[u] = True
            elif v!= parent[u]:
                low[u] = min(low[u],disc[v])
    
    def articulation_point(self):
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)
        ap = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                self.articulation_point_util(i,visited,ap,parent,low,disc)
        for index,value in enumerate(ap):
            if value == True: print(index,end=" ")
graph_articulation = Graph_Articulation(5)
graph_articulation.add_edge(1,0)
graph_articulation.add_edge(0,2)
graph_articulation.add_edge(2,1)
graph_articulation.add_edge(0,3)
graph_articulation.add_edge(3,4)
print("Articulation Point in the graph: ")
graph_articulation.articulation_point()
print("\n")

"""
Bridge in Graph
    - Rule : low[v]>discovery[u]
"""
class Graph_Bridge:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def add_Edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bridge_util(self,u,visited,parent,low,disc):
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time +=1

        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                self.bridge_util(v,visited,parent,low,disc)
                low[u] = min(low[u],low[v])
                if low[v]>disc[u]:
                    print("%d %d"%(u,v))
            elif v!= parent[u]:
                low[u] = min(low[u],disc[v])

    def bridge(self):
        visited = [False] * self.V
        disc = [float("Inf")] * self.V
        low = [float("Inf")] * self.V
        parent = [-1] * self.V
        
        for i in range(self.V):
            if visited[i] == False:
                self.bridge_util(i,visited,parent,low,disc)

graph_bridge = Graph_Bridge(5)
graph_bridge.add_Edge(1,0)
graph_bridge.add_Edge(0,2)
graph_bridge.add_Edge(2,1)
graph_bridge.add_Edge(0,3)
graph_bridge.add_Edge(3,4)
print("Bridge in the Graph: ")
graph_bridge.bridge()
print()

"""
Tarjan's Algorithm:
    - If all adjacent a vertex 4  are sone with recursive and disc[u] = low[u], then print this vertex all others in a stack
    - Back Edge : The edge which goes back to ancestor
    - Cross Edge : The edge which goes back to some other node
"""
class Graph_Tarjan:
    def __init__(self,vertices):
        self.V =vertices
        self.graph = defaultdict(list)
        self.Time = 0
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def tarjan_util(self,u,low,disc,stackMember,st):
        disc[u] = self.Time
        low[u] = self.Time
        self.Time+=1
        stackMember[u] = True
        st.append(u)

        for v in self.graph[u]:
            if disc[v]==-1:
                self.tarjan_util(v,low,disc,stackMember,st)
                low[u] = min(low[u],low[v])
            elif stackMember[v] == True:
                low[u] = min(low[u],disc[v])
        
        w = -1
        if low[u] == disc[u]:
            while w!=u:
                w = st.pop()
                print(w,end = " ")
                stackMember[w] = False
            print()
        
    def tarjan(self):
        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stackMember = [False] * (self.V)
        st = []
        for i in range(self.V):
            if(disc[i] == -1):
                self.tarjan_util(i,low,disc,stackMember,st) # type: ignore
graph_tarjan = Graph_Tarjan(5)
graph_tarjan.add_edge(1,0)
graph_tarjan.add_edge(0,2)
graph_tarjan.add_edge(2,1)
graph_tarjan.add_edge(3,4)
print("Tarjan Algorithm of strongly connected component: ")
graph_tarjan.tarjan()
print("\n")

"""
Kruskal's Algorithm
    - Spanning : still a path from vertex to each vertex and it should be tree and no cycle must exist.

Algorithm : 
    - Sort all edges in increasing order
    - Initialize : MST = [],res = 0
    - Do following for every edge 'e' while MST size does not become V-1
        - if Adding e to MST does not cause a cycle 
            = MST = MST U {e}
            = res = res + e.weight
    - return res
Time Complexity : O(E*log(E) + V + E) = O(E*log(E))
"""
class Graph_Kruskal:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])
    
    def apply_union(self,parent,rank,x,y):
        x_root= self.find(parent,x)
        y_root= self.find(parent,x)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] +=1
    
    def kruskal(self):
        result = []
        i,e = 0, 0
        self.graph = sorted(self.graph,key = lambda item:item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e<self.V - 1:
            u,v,w = self.graph[i]
            i= i + 1
            x = self.find(parent,u)
            y = self.find(parent,v)
            if x!= y:
                e = e + 1
                result.append([u,v,w])
                self.apply_union(parent,rank,x,y)
        for u,v,weight in result:
            print("%d - %d : %d"%(u,v,weight))
graph_kruskal = Graph_Kruskal(6)
graph_kruskal.add_edge(0,1,4)
graph_kruskal.add_edge(0,2,4)
graph_kruskal.add_edge(1,2,2)
graph_kruskal.add_edge(1,0,4)
graph_kruskal.add_edge(2,0,4)
graph_kruskal.add_edge(2,1,2)
graph_kruskal.add_edge(2,3,3)
graph_kruskal.add_edge(2,5,2)
graph_kruskal.add_edge(2,4,4)
graph_kruskal.add_edge(3,2,3)
graph_kruskal.add_edge(3,4,3)
graph_kruskal.add_edge(4,2,4)
graph_kruskal.add_edge(4,3,3)
graph_kruskal.add_edge(5,2,2)
graph_kruskal.add_edge(5,4,3)
print("Kruskal's Algorithm (Minimum Spanning Tree) : ")
graph_kruskal.kruskal()
print("\n")