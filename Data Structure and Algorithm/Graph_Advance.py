"""
GRAPH DATA STRUCTURE
"""

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