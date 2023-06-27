#Big 'O' notation Coding examples

"""
Big-O Asymptotic Notation
    - it is use for comparing code1 an code2 mathematically.
    - Comparison based on time complexity
    - There is another comparison known as space complexity.
    - Big O means worst case scenario

"""

print("Hello World")

#this code will run of O(n) and have straight linear graph.
def print_items(n):
    for i in range(n):
        print(i);
