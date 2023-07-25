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
    
"""
Open Addressing
    - No. of slots in Hash Table >= No. of Keys to be inserted
    - Cache Friendly
    - Linear Probing Method : For handling collision, linearly search for next empty slot
    - Hash Function: key % 7

    Search Function: 
        - We Compute hash function we go to that index and compare if we find, we return True. Otherwise we linearly Hash. We stop when one of the three cases arise, Empty Set, Key Found, Traverse throughout Array.
    
    Delete Function:
        - In Delete Function we used to delete the element but in the hash table we will mark it as delete. So, that it doesn't hamper search function. Because if search see an empty slot it will stop working.
    
    Clustering (A problem of Linear Probing)
        - Quadratic Probing = (H(key) + l^2) % m
        - Double Hashing = (H1(key) + i*H2(key)) % m
    
    Fact: if Load Factor < 0.5 and , m is prime then quadratic probing guarantee to work.


    Double Hashing
        - hash(key,i) = [h1(key) + i*(h2(key))] % m
        - If h2(key) is relatively prime to m, then it always find a free slot if there is one.
        - Distributes keys more uniformly than linear probing and quadratic hashing
        - No Clustering
        - h2 cannot be zero, h2 = N - (key % N)

        Algorithm Of Double Hashing

            void doubleHashingInsert(key):
                if (table is full):
                    return error
                probe = h1(key), offset = h2(key)
                
                while(table[probe] is occupied):
                    probe = (probe + offset) % m
                table[probe] = Key
"""
"""
Problem Statement: Find frequencies of Array element.

I/P: l = [10,12,10,15,10,10,20,12,12]
O/P: 10 - 3, 12 - 3, 15 - 1,20 - 1
"""
def frequency_element_naive(l):
    for i in range(len(l)):
        flag=False
        for j in range(i):
            if l[i] == l[j]:
                flag=True
                break
        if flag == True:
            continue
        freq = 1
        for j in range(i+1,len(l)):
            if l[i] == l[j]:
                freq+=1
        print(l[i]," : ",freq)
frequency_element_naive([50,50,10,40,10])

def frequency_element(arr):
    hmp = dict()
    for i in range(len(arr)):
        if arr[i] in hmp.keys():
            hmp[arr[i]]+=1
        else:
            hmp[arr[i]] = 1
    for i in hmp:
        print(i," : ",hmp[i])
print()
frequency_element([50,50,10,40,10])
# Time Complexity: O(n)
# Auxiliary Space: O(n)

"""
Open Addressing Implementation
    - Using Linear Probing to handle collision
"""

class OpenAddressHash:
    def __init__(self,c):
        self.cap=c
        self.table = [-1]*c
        self.size=0
    
    def hash(self,x):
        return x % self.cap
    
    def search(self,x):
        h=self.hash(x)
        t=self.table
        i=h
        while t[i]!=-1:
            if t[i] == x:
                return True
            i = (i+1)%self.cap
            if i == h:
                return False
            return False
    
    def insert(self,x):
        if self.size == self.cap:
            return False
        if self.search(x) == True:
            return False
        i = self.hash(x)
        t = self.table
        while t[i] not in (-1,-2):
            i = (i+1) % self.cap
        t[i] = x 
        self.size = self.size+1
        return True
    
    def remove(self,x):
        h = self.hash(x)
        t = self.table
        i=h
        while t[i]!=-1:
            if t[i] == x:
                t[i] = -2
                return True
            i = (i+1)%self.cap
            if i ==h:
                return False
        return False