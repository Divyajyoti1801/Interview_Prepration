"""
Problem - 8 :  DEPTH-FIRST-SEARCH of a Graph

Problem Statement : 
    - You are given a connected undirected graph. Perform a Depth First Traversal of the graph.
    - Note: Use the recursive approach to find the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph.

Input : V = 5, adj = [[2,3,1],[0],[0,4],[0],[2]]
Output : 0 2 4 3 1
"""
class Adjacency_Node:
    def __init__(self,data):
        self.vertex = data
        self.next = None
