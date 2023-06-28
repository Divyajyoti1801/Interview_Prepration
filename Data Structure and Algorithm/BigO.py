#Big 'O' notation Coding examples

"""
Big-O Asymptotic Notation
    - it is use for comparing code1 an code2 mathematically.
    - Comparison based on time complexity
    - There is another comparison known as space complexity.
    - Big O means worst case scenario

O(1) < O(log(n)) < O(n) < O(nlog(n)) < O(n^2) < O(2^n) < O(n!)

"""

print("Hello World")


#this code will run of O(n) and have straight linear graph.
def print_items(n):
    for i in range(n):
        print(i);
    
    for j in range(n):
        print(j);
    
    # now this code run O(n+n) times, O(2n) but we will drop the constant and it will be O(n) 


#this code will run O(n^2) and have hyperbolic graph
def print_items_2(n):
    for i in range(n):
        for j in range(n):
            print(i,j);

#Example for dropping non-Dominants
def print_items_3(n):
    for i in range(n):
        for j in range(n):
            print(i,j);
    
    for k in range(n):
        print(k)
 #Time complexity of this is basically O(n^2 + n) but n is non dominant against n^2 so time complexity will be O(n^2)

#this code will run O(1) times, most efficient code the graph will flat line at the bottom 
def add_items(n):
    return n+n+n;

#Merge sort is the example for O(log(n)) complexity. because of division of data structure.

#Different terms for input
def print_items_4(a,b):
    for i in range(a):
        print(i);

    for j in range(b):
        print(j);

    # So time complexity will be O(a+b) it will a!=n && b!=n. These are two different entities

#Time Complexity of the list start and end of the list push and pop will be O(1). but at any other position it will be O(n)