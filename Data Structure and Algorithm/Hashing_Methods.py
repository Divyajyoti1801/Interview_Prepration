"""
HASHING METHOD

    Introduction To Hashing
        - Search O(1) 
        - Insert O(1)
        - Delete O(1)
        - use for implementation of Dictionary
    
    Not Used For:
        - Finding Client Value [AVL Tree or Red-Black Tree]
        - Sorted Data
        - Prefix Searching [Tri Data Structure]
    
    Applications Of Hashing:
        - Dictionaries
        - Database Indexing
        - Cryptography
        - Caches
        - Symbol Tables in Compilers / Interpreters
        - Routers
        - Caches
        - Getting data from databases
"""

"""
DIRECT ADDRESS TABLE : main Concept of Hashing
    - Imagine a situation where you have 1000 keys with values from (0 to 999), how would you implement following in O(1) time.
        - Search
        - Insert
        - Delete
    
    SOLUTION:
        - Create a boolean list of 1000
        - insert operation insert(99) then go to the index and change value from False to True. Time Complexity: O(1)
        - delete operation delete(99) then change from True to False. Time Complexity: O(1)
    
    - Hash Tables cannot handle large keys and floating point variables.
"""

"""
HASHING INTRODUCTION

Universe Of Keys ---> Hash Functions  ---> List
Example:
    - Phone Numbers 
    - Email
    - API Key

Hashing Function: hashing functions are used to map universal keys to array indexes for efficient storage and retrieval.

How Hash Functions Work:
    - Should always map a larger key to same small key.
    - Should generate values from O to m-1
    - Should be fast, O(1) for integers and O(len) for string of length "len"
    - Should uniformly distribute larger keys into Hash Table slots.

Example Of Hash Functions:
    - h(large_key) = large_key % m
    - For strings, Weighted sum : str[] = "abcd"
       (str[0]  * x^0 + str[1] * x^1 + .....) % m
    - Universal Hashing: randomly pick the hash functions.
"""

"""
COLLISION HANDLING
    - if we know keys in advance, then we can Perfect Hashing, If we do not know keys, then we use one of the following
        - Chaining 
        - Open Addressing
            - Linear Probing
            - Double Hashing
            - Quadratic Probing
    
1st Method: Chaining
    - Create an Array of Linked List Headers.
    - Hash function: Key % 7
    - Keys = {50,21,58,17,15,49,56,22,23,25}

    Performance:
        m = no. of slots in Hash Tables
        n = no. of Keys to be inserted
        Assumption : Keys are uniformly segregated
        Load Factor = n/m

        Expected Chain Length: Load Factor
        Expected Time to Search: O(1 + Load Factor)
        Expected Time to Insert/Delete: O(1 + Load Factor)
    
    Data Structures for storing Chains:
        - Linked List
        - Dynamic Sized Arrays
        - Self Balancing BST (AVL Tree, Red Black Tree)
"""
"""
Implementation Of Chaining:
    - BUCKET = Which is list of lists
    - Hash Function: x % BUCKET_SIZE
"""
class SelfHash:
    def __init__(self,b):
        self.BUCKET=b
        self.table = [[] for x in range(b)]
    
    def insert(self,x):
        i = x % self.BUCKET
        self.table[i].append(x)
    
    def remove(self,x):
        i = x % self.BUCKET
        self.table[i].remove(x)
    
    def search(self,x):
        i = x % self.BUCKET
        return x in self.table[i]