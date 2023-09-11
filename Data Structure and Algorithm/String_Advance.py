"""
ADVANCE STRING CONCEPTS AND QUESTIONS
"""

"""
Problem Statement: Pattern Searching Problem

Pattern Searching Algorithms:
    - Naive: O((n-m+1)*m), Naive when all characters of pattern are distinct: O(n)
    - Rabin Karp Algorithm: O((n-m+1)*m) But better than naive approach
    - KMP: O(n)
    - Suffix Tree: O(m)
"""
def pattern_searching_1(S="",pattern=""):
    res = []
    pos=S.find(pattern)
    while pos>=0:
        res.append(pos)
        pos = S.find(pattern,pos+1)
    return res 
print("Pattern Searching (Naive): ",pattern_searching_1("geeks for geeks","geeks"))
print()

def naive_pattern_searching_algo(S="",pattern=""):
    res = []
    m = len(pattern)
    n = len(S)
    for i in range(n-m+1):
        j = 0
        while j<m:
            if pattern[j] != S[i+j]:
                break
            j+=1
        if j == m:
            res.append(i)
    return res
print("Naive Pattern searching problem: ",naive_pattern_searching_algo("ABABABCD","ABAB"))
def improved_naive_pattern_searching_algo(S="",pattern=""):
    m,n = len(pattern),len(S)
    res = []
    i = 0 
    j=0
    while i<= (n-m):
        for j in range(m):
            if pattern[j] != S[i+j]:
                break
            j+=1
        if j == m:
            res.append(i)
        if j == 0:
            i+=1
        else:
            i+=j
    return res
print("Improved naive searching pattern (Pattern with Distinct Element): ",improved_naive_pattern_searching_algo("ABCEABFABCD","ABCD"))
print()

"""
Rabin Karp Algorithm: Pre-Processing Pattern Searching Algorithm
    Rolling Hash : Ti+1 = D(Ti - (T*T) * (D^(m-1))) + (t * t[i+m]) m = Length of pattern
    Creating Hash : D = 5 ; h("abc") = 1*(d^2) + 2*(d^1) + 3*(d^0) = 1*25 + 2*5 + 3*1 = 38 
    
    Time Complexity: O((n-m+1)*m)
"""
D = 256
def rabin_karp_algo(pattern,S,q):
    m,n = len(pattern),len(S)
    res = []
    h = 1
    for i in range(1,m):
        h = (h*D) % q
    p,t = 0,0
    for i in range(m):
        p = (p*D*ord(pattern[i]))%q
        t = (t*D*ord(pattern[i]))%q
    # Checking for Spurious Hit
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if S[i+j]!=pattern[j]:
                    break
            else:
                res.append(i)
        if i < (n-m):
            t = ((D*(t - ord(S[i])*h)) + ord(S[i+m])) % q
        if t < 0:
            t+=q
    return res
print("Rabin Karp Algorithm: ",rabin_karp_algo("GEEK","GEEKS FOR GEEKS",101))
print()

"""
KMP Algorithm : Pre-Processing Algorithm 
  - Step 1: Constructing Longest Proper Prefix Suffix Array
        - If str[i] and str[len] match
            lps[i] = len+1, len++
        - If str[i] and str[len] Do not match
            = If len = 0; lps[i] = 0
            = Else len = lps[len-1]; we now compare str[i] and str[len]
"""
def longest_proper_prefix_suffix_naive(S,n):
    for l in range(n-1,-1,-1):
        for j in range(l):
            if S[j]!= S[n-l+j]:
                break
            else:
                return l

    return 0

def fill_LPS_Array(S,lps=[]):
    lps[0]=0
    for i in range(1,len(S)):
        lps[i] = longest_proper_prefix_suffix_naive(S,i+1)


def longest_proper_prefix_suffix(S):
    lps =[0]*len(S)
    i = 1
    l = 0
    while i<len(S):
        if S[i] == S[l]:
            l += 1
            lps[i] = 1
            i+=1
        else:
            if l != 0:
                l = lps[l-1]
            else:
                lps[i] = 0
                i+=1
    res = lps[len(S)-1]
    if res > len(S)/2:
        return len(S)//2
    else:
        return res
print("Firs step of KPM Algo Longest Proper Prefix Suffix O(n): ",longest_proper_prefix_suffix("abcab"))
print()
"""
Part 2: KMP Algorithm
    - Time Complexity: O(n)
    - It use longest Proper Prefix Suffix Algorithm
    - The naive algorithm works really efficiently when the string characters are distinct.
"""

"""
Problem Statement : Anagram Search
I/P: txt = "geeksforgeeks" pat = "frog"
O/P: Yes
"""
CHAR = 256
def is_present(txt,pattern):
    n = len(txt)
    m = len(pattern)
    for i in range(n-m+1):
        if anagram_search_1(txt,pattern,i):
            return True
    return False
def anagram_search_1(txt,pat,i):
    count = [0] * CHAR
    for j in range(len(pat)):
        count[ord(pat[j])]+=1
        count[ord(txt[i+j])]-=1
    for j in range(CHAR):
        if count[j]!=0:
            return False
    return True
print("Is Anagram string present in the given string (Naive): ",is_present("geeksforgeeks","frog"))
"""
Efficient Approach: Using sliding window technique
"""
def are_same(ct,cp):
    for i in range(CHAR):
        if ct[i] != cp[i]:
            return False
    return True

def isPresent(text,pattern):
    n = len(text)
    m = len(pattern)
    ct = [0]*CHAR
    cp = [0]*CHAR
    for i in range(m):
        ct[ord(text[i])]+=1
        cp[ord(pattern[i])]+=1
    for i in range(m,n):
        if are_same(ct,cp):
            return True
        ct[ord(text[i])]+=1
        ct[ord(text[i-m])]-=1
    return False
print("Is Anagram chain of string present in the given string (Effective): ",isPresent("geeksforgeeks","frog"))
print()
"""
Problem Statement: Lexicographic Rank  
"""
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
def lexicographic_rank(S):
    res = 1
    n = len(S)
    mul = factorial(n)
    count =[0]*CHAR
    for i in range(n):
        count[ord(S[i])]+=1
    for i in range(1,CHAR):
        count[i]+=count[i-1]
    for i in range(n-1):
        mul = mul//(n-i)
        res += count[ord(S[i])-1] * mul
        for j in range(ord(S[i]),CHAR):
            count[j]-=1
    return res
print("Lexicographical Rank of a string: ",lexicographic_rank("STRING"))
print()

"""
Problem Statement: Longest Substring with Distinct Characters
"""
def Are_Distinct(str,i,j):
    visited = [0]*CHAR
    for k in range(i,j+1):
        if visited[ord(str[k])] == True:
            return False
        visited[ord(str[k])] = True
    return True
def longest_substring_distinct_characters_1(S):
    n = len(S)
    res = 0
    for i in range(n):
        for j in range(i,n):
            if Are_Distinct(S,i,j):
                res = max(res,j-i+1)
    return res
print("Longest Substring with distinct characters (Method-1): ",longest_substring_distinct_characters_1("abcdabc"))
def longest_substring_distinct_characters_2(S):
    n = len(S)
    res = 0
    for i in range(n):
        visited = [0] * 256
        for j in range(i,n):
            if visited[ord(S[j])] == True:
                break
            else:
                res = max(res,j-i+1)
                visited[ord(S[j])] = True
    return res
print("Longest Substring with distinct characters (Method-2): ",longest_substring_distinct_characters_2("abcdabc"))
def longest_substring_distinct_characters_3(S):
    n = len(S)
    res = 0
    prev = [-1] * 256
    i = 0
    for j in range(n):
        i = max(i,prev[ord(S[j])]+1)
        max_end = j-i+1
        res = max(res,max_end)
        prev[ord(S[j])] = j
    return res
print("Longest Substring with distinct characters (Method-3): ",longest_substring_distinct_characters_3("abcdabc"))