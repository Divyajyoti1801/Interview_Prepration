"""
RECURSION METHOD
    - Function which call itself directly or indirectly in order to solve a big problem by solving small problems is know as recursion.
"""

def func_1(n):
    if(n<=0):
        return
    print("GFG")
    return func_1(n-1)

func_1(5)

"""
Applications Of Recursion
    - Many algorithm technique are based on Recursion.
        - Dynamic Programming
        - Backtracking
        - Divide and Conqueror (Binary Search, Quick Sort and Merge Sort)
    - Many Problems inherently recursive
        - Tower Of Hanoi
        - DFS based traversal (DFS of graph and Inorder traversal/PreOrder/PostOrder traversal of true)
"""

"""
How To Write Base Case in Recursion
"""
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print("Factorial Of The Number: ",factorial(5))

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print("Fibonacci Number: ",fibonacci(5))

"""
Tail Recursion
    - A recursive function is called Tail recursive if the function does not do any thing after the last recursive call.
    
    - Example of Tail Recursive Functions
        - Quick Sort
        - PostOrder Tree Traversal
"""

# Practice of Recursion
def func_2(n):
    if n==0:
        return
    print(n)
    func_2(n-1)
    print(n)

print("Practice Function-2")
func_2(3)

def func_3(n):
    if n==0:
        return
    func_3(n-1)
    print(n)
    func_3(n-1)
print("Practice Function-3")
func_3(3)

def func_4(n):
    if n<=1:
        return 0
    else:
        return 1 + func_4(n/2)
print("Practice Function-4")
print(func_4(16))

def fun_5(n):
    if n==0:
        return
    fun_5(n//2)
    print(n%2)
print("Practice Function-5")
fun_5(13)

"""
Problem Statement: print 1 to n using recursion.

I/P: n = 4
O/p: 1 2 3 4
"""
def print1ToN(n):
    if n==0:
        return
    print1ToN(n-1)
    print(n)
print()
print1ToN(5)

"""
Problem Statement: Print n to 1 using recursion.
I/P: n=5
O/P: 5 4 3 2 1
"""
def printNto1(n):
    if n==0:
        return
    print(n)
    printNto1(n-1)
print()
printNto1(5)

"""
Problem Statement: Sum of Digits

I/P: n = 253
O/P: 10
"""
def sumOfDigit(n):
    if n<10:
        return n
    return sumOfDigit(n//10) + n % 10
print("Sum of Digit: ",sumOfDigit(253))

"""
Problem Statement: is string palindrome
I/P: abba
O/P: yes
"""

def isPalindromeOps(st,s,e):
    if (s==e):
        return True
    if(st[s] != st[e]):
        return False
    if(s<e+1):
        return isPalindromeOps(st,s+1,e-1)
    return True

def isPalindrome(st):
    n = len(st)
    if(n==0):
        return True
    return isPalindromeOps(st,0,n-1)

print("Is string Palindrome: ",isPalindrome("abba"))