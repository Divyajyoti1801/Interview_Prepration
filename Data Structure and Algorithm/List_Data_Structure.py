# DATA STRUCTURE
"""
List Introduction
    - Dynamic Size
    - Allows items of different types
"""

list_1=[10,20,30,40,50]
print(list_1)
print(list_1[3])
print(list_1[-1])
print(list_1[-2])

# Append function on list
list_1.append(30)
print(list_1)

# Insert function on list
list_1.insert(1,15)
print(list_1)

# Search function in list
print(15 in list_1)

# Count function in list
print(list_1.count(30))

# Index Checking of element in list
print(list_1.index(30)) # 1-form
print(list_1.index(30,4,7)) # 2-form 

# Removal of element in list
list_1.remove(20)
print(list_1)

# Removal of element from last
print(list_1.pop())
print(list_1)

# Removal from position
print(list_1.pop(3))
print(list_1)

# Delete item
del list_1[1]
print(list_1)

# Delete range of element in list
del list_1[0:2]
print(list_1)

list_2=[10,40,20,50]
print(list_2)

# Largest element of list
print(max(list_2))

# Smallest element of list 
print(min(list_2))

# Sum of all elements of the list 
print(sum(list_2))

# Reveres of list
list_2.reverse()
print(list_2)

# Sorting of list
list_2.sort()
print(list_2)


""""
Working Of List In Python

    Advantages
        - Random Access
        - Cache Friendly
        - Preallocated extra space
    
    Disadvantages
        - Insertion, Deletion  are slow
        - Search is also slow for unsorted.
        
How Does Dynamic Size Work?
    - Preallocate some extra space.
    - If becomes full, do the following.
        - Allocate a new space of larger size (multiply by x)
        - Copy old space to new
        - Free old space

Amortized Time
    - Initial Capacity: n
    - We double the size when become full 
    - Average Time to append (n+1) items = theta(1)
"""

# Average Or Mean Of A List 
"""
Problem Statement: Find the average of a mean of a list.

I/P : l = [10,20,30,40]
O/P : 25.0
"""
def mean_of_list(list_1):
    avg = sum(list_1) / len(list_1)
    return avg

print("Average Of a List: ",mean_of_list([30,60,40]))

# Separate Even And Odd
"""
Problem Statement: Separate even and odd from the list.

I/P : l = [10,41,30,15,80]
O/P : even = [10,30,80]
      odd = [41,15]
"""
def even_and_odd(list_1):
    even_list=[]
    odd_list=[]
    for i in list_1:
        if(i%2==0):
            even_list.append(i)
        else:
            odd_list.append(i)
    print("Even Element of the list: ", even_list)
    print("Odd Element of the list: ", odd_list)

even_and_odd([10,41,30,15,80])

"""
Problem Statement: get smaller elements from the list with respect to mentioned number

I/P : l = [8,100,20,40,3,7] x = 10
O/P : [8,3,7]
"""

def get_smaller_elements(list_1,x):
    result_list=[]
    list_1.sort()
    for i in list_1:
        if(i<x):
            result_list.append(i)
        
    return result_list

print(get_smaller_elements([8,100,20,40,3,7],10))

"""
Slicing (List, Tuple and String)

Concept:
    - l[start:stop:step]: Gives a list with elements l[start], l[start + step], l[start + 2*stop]... stop is not included (We Stop before step)

I/P : l = [10,20,30,40,50]
O/P : [10,30,50]
"""
list_3=[10,20,30,40,50]
print(list_3[:4])
print(list_3[2:])
print(list_3[1:4])
print(list_3[4:1:-1])
print(list_3[::-1]) # reverse of the list

list_c_3=list_3[:]
print(list_c_3 is list_3) # New List Created

tuple_1 = (10,20,30)
tuple_c_1 = tuple_1[:]
print(tuple_1 is tuple_c_1) # No new tuple is created

string_1 = "geeks"
string_2 = string_1[:]
print(string_1 is string_2) # No new string is created 

"""
Comprehensions In Python
    - it is possible because list,tuple and string are iterable in nature.
"""
list_4 = [x for x in range(11) if x % 2 == 0]
print(list_4)

list_5 = [x for x in range(11) if x % 2 != 0]
print(list_5)

def get_smaller_compre(l,x):
    return [e for e in l if e < x]
print(get_smaller_compre([9,15,12,3,7,11],10))

string_3="geeksforgeeks"
print([x for x in string_3 if x in "aeiou"])

list_5 = ["geeks","ide","courses","gfg"]
print([x for x in list_5 if x.startswith("g")])
print([x.upper() for x in list_5 if x.startswith("g")])

print([x*2 for x in range(6)])

list_6=[1,3,4,2,5]
print({x:x**3 for x in list_6})

print({x:f"ID{x}" for x in range(5)})

list_7=[101,103,102]
list_8=["gfg","ide","course"]
print({list_7[i]:list_8[i] for i in range(len(list_7))})

dict_1=dict(zip(list_7,list_8))
print(dict_1)

"""
Dictionary Comprehension
    - Inverting a dictionary (key becomes value) and value becomes key
"""
print({v:k for (k,v) in dict_1.items()})

"""
Largest Element in a List

Problem Statement: Find the largest element in the list.

I/P : l = [10,5,20,8]
O/P : 20
"""
def getMaxOfList(l):
    if not l:
        return None
    else:
        res=l[0]
        for i in range(1,len(l)):
            if l[i]>res:
                res=l[i]
        return res;
print("Largest Element Of The List: ",getMaxOfList([10,5,20,8]))

"""
Second Largest Element In A List

Problem Statement: find the second largest element of the list.

I/P: l = [10,5,8,20]
O/P: 12
"""
def second_largest(l):
    if len(l)<=1:
       return None
    lar = l[0]
    slar = None
   
    for x in l[1:]:
        if x > lar:
            slar= lar
            lar = x
        elif x!=lar:
            if slar == None or slar < x:
                slar= x
    return slar

print(second_largest([10,5,8,20]));

"""
Problem Statement: Check if a list is sorted.

I/P: [10,32,30]
O/P: True
"""
def check_sorted(l):
    i=1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i+=1
    return True
print(check_sorted([10,20,30,15,40]))

"""
Problem Statement: reverse of the list in python
"""
def reverse_list(l):
    return l[::-1]

def reverse_list_2(l):
    s=0
    e = len(l)-1
    while s<e:
        l[s],l[e]=l[e],l[s]
        s=s+1
        e=e-1
    return l
print(reverse_list([10,20,30,40]))
print(reverse_list_2([10,20,30]))

"""
Problem Statement: Remove duplicate from a sorted array
"""
def remove_duplicate(l):
    res=1
    for i in range(1,len(l)):
        if l[res-1]!=l[i]:
            l[res]=l[i]
            res+=1
    return res;

print(remove_duplicate([10,20,20,30,30,30,30]))

"""
Problem Statement: left rotate the list by 1
"""

def left_rotate(l):
    n = len(l)
    x = l[0]
    for i in range(1,n):
        l[i-1] = l[i]
    l[n-1] = x
    return l;
print(left_rotate([10,20,30,40]))

def left_rotate_2(l):
    l.append(l.pop(0))
    return l
    

print(left_rotate_2([10,20,30,40]))