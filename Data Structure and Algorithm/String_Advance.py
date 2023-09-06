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
def longest_proper_suffix(S):
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
print("Firs step of KPM Algo Longest Proper Suffix O(n): ",longest_proper_suffix("abcab"))