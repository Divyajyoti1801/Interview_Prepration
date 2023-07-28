"""
STRINGS IN PYTHON

    - Sequence of character
    - use to store text data like data read from a file
    - Typically small set of character
    - Characters 'A' to 'Z' are stored as values from 65 to 90
    - Characters 'a' to 'z' are stored values from 97 to 122
    - Strings are immutable
"""
print("Integer representation of a character: ",ord('a'))
print()
print("Character representation of an Integer: ",chr(97))
print()
string_1="geeksForgeeks"
print(string_1)
print(string_1[0])
print(string_1[-1])
print(string_1[1])
print(string_1[-2])
print("Reverse of the String: ",string_1[::-1])

string_2 = """
This is a GeeksForGeeks Data Structure and Algorithm in
Python course. For holistic learning. Hope you are enjoying it.
"""
print()
print("Multi-line String ",end=":")
print(string_2)

string_3 = "Welcome to Geek\'s Course"
print("Escape sequence String:" , string_3)
string_4 = r"C:\project\name.py"
print("Raw String: ",string_4)

s_1 = "ABC"
s_2 = "Python Course"
string_5 = f"Welcome {s_1} to the {s_2}"
print("Formatted String: ",string_5)
print()

string_6="geeksforgeeks"
string_7="ide"
print("string_6 < string_7: ",string_6<string_7)
print("string_6 <= string_7: ",string_6<=string_7)
print("string_6 > string_7: ",string_6>string_7)
print("string_6 >= string_7: ",string_6>=string_7)
print("string_6 == string_7: ",string_6==string_7)
print("string_6 != string_7: ",string_6!=string_7)
print()

print("String Operations")
print("string_7 is substring of string_8: ",string_7 in string_6)
print("string_7 is not substring of string_8: ",string_7 not in string_6)
string_8= string_6 + string_7
print("Concatenation of the strings: ",string_8)
string_9 = "geeks"
print("index of substring: ",string_6.index(string_9))
print("Last index of substring: ",string_6.rindex(string_9))
print("Length of the string: ",len(string_9))
print("Uppercase of the string: ",string_9.upper())
print("Lowercase of the string: ",string_9.lower())
print("Is Lowercase: ",string_9.islower())
print("Is Uppercase: ",string_9.isupper())
string_10 = "GeeksforGeeks Python Course"
print(string_10.startswith("Geeks"))
print(string_10.endswith("Course"))
print(string_10.startswith("Geeks",1))
print(string_10.startswith("Geeks",8,len(string_10)))
string_11 = "geeks for geeks"
print("Splitting of the string: ",string_11.split())
print("Splitting of the string: ",string_11.split(","))
list_1 = ["geeksforgeeks","python","course"]
print("Joining of string: "," ".join(list_1))
print("Joining of string: ",", ".join(list_1))
string_12 = "---geeksforgeeks---"
print("Striping unnecessary part: ",string_12.strip("-"))
print("Striping unnecessary part: ",string_12.lstrip("-"))
print("Striping unnecessary part: ",string_12.rstrip("-"))
print("Find string inside the string: ",string_6.find(string_9))
print("Find string inside the string: ",string_6.find("gfg"))

"""
Problem Statement: Reverse the given string
I/P: "geek"
O/P: "keeg"
"""
def reverse_string(s):
    return s[::-1]
print("Reverse of the string: ",reverse_string("geek"))

def reverse_string_loop(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev
print("Reverse of the string using loop: ",reverse_string_loop("geek"))

"""
Problem Statement: check for rotation
I/P: s1 = "ABCD" , s2 = "CDAB"
O/P: Yes
"""
def check_rotation(s1,s2):
    if len(s1)!=len(s2) and len(s1)<=0 and len(s2)<=0:
        return False
    temp = ""
    temp = s1+s2
    return temp.find(s2)!=-1
print("Is string rotated: ",check_rotation("ABCD","CDAB"))

def check_palindrome(s):
    low  = 0
    high = len(s)-1
    while low<high:
        if s[low]!=s[high]:
            return False
        low+=1
        high-=1
    return True
print("Check Palindrome Loop: ",check_palindrome("10022001"))

def check_for_palindrome(s):
    rev = s[::-1]
    if s == rev:
        return True
    return False
print("Check Palindrome: ",check_for_palindrome("10022001"))

"""
Problem Statement : check if a string is a subsequence of other
I/P: s1 = "ABCD"
     s2 = "AD"
O/P: True
"""
def check_subsequence_naive(s1,s2):
    i=j=0
    while i<len(s1) and j<len(s2):
        if s1[i] == s2[j]:
            j+=1
        i+=1
    if j == len(s2):
        return True
    return False
print("Is subsequence: ",check_subsequence_naive("ABCDEF","ADE"))

# def inSubSeq(s1,s2,m,n):
#     if n == 0:
#         return True
#     if m == 0:
#         return False
#     if s1[n-1] == s2[m-1]:
#         return inSubSeq(s1,s2,m-1,n-1)
#     else:
#         return inSubSeq(s1,s2,m-1,n)
# print("Is Subsequence: ", inSubSeq("ABCDEF","ADE",len("ABCDEF"),len("ADE")))

"""
Problem Statement: check for anagrams
I/P: s1 = "listen" s2 = "silent"
O/P: Yes
"""
def check_anagram_naive(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2
print("Check for anagram live: ",check_anagram_naive("abaac","aacba"))

def check_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    count = [0]*256
    
    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1
    
    for x in count:
        if x!=0:
            return False
    return True
print("Check for anagram live: ",check_anagram("abaac","aacba"))

"""
Problem Statement: Left most repeating character 
I/P: str = "geeksforgeeks"
O/P: 0
"""
def leftmost_repeating_string(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return i
    return -1
print("Left most repeating occurrence: ",leftmost_repeating_string("cabbad"))

def leftmost_repeating(s):
    count = [0] * 256
    for i in range(len(s)):
        count[ord(s[i])]+=1
    for i in range(len(s)):
        if count[ord(s[i])]>1:
            return i
    return -1
print("Left most repeating occurrences: ",leftmost_repeating("cabbad"))

"""
Problem Statement: Leftmost non repeating element
I/P: s= "One"
O/P: False
"""
def leftmost_non_repeating_string(s):
    for i in range(len(s)):
        flag = False
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                flag = True
                break
            if flag == False:
                return i
    return -1
print("Leftmost non repeating element: ",leftmost_non_repeating_string("One"))

def leftmost_non_repeating(s):
    count = [0] * 256
    for i in s:
        count[ord(i)]+=1
    for i in range(len(s)):
        if count[ord(s[i])]==1:
            return i
    return -1
print("Leftmost non repeating element: ",leftmost_non_repeating("One"))

"""
Problem Statement: reverse words in the string
I/P: s = "Welcome to dsa"
O/P: "dsa to Welcome"
"""
# def reverse(s,b,e):
#     while(b<e):
#         s[b],s[e]=s[e],s[b]
#         b+=1
#         e-=1

# def reverse_words(s):
#     n = len(s)
#     b = 0
#     for e in range(n):
#         if s[e] == ' ':
#             reverse(s,b,e-1)
#             b=e+1
#         reverse(s,b,e-1)
#         reverse(s,0,n-1)
            
# print("Reverse of words in the string: ",reverse_words("Welcome to dsa"))