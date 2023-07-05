"""
Analysis of Algorithm

"""

# solution 1
def sum_of_natural_numbers(n):
    sum=0
    for i in range(n+1):
        sum+=i
    
    print(sum)
sum_of_natural_numbers(10)
#order of growth: C2n + C3 (linear growth)

#solution 2
def sum_of_natural_numbers_2(n):
    return n*(n+1)/2
#order of growth: C1 (no growth)

#solution 3
def sum_of_natural_numbers_3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum=sum+j
    
    return sum
#order of growth: C4(n^2) + C5n + C6 (quadratically growth)
"""
Asymptotic Analysis (Theoretical Analysis):
    - No dependency on machine programming language etc.
    - We do not have to implement all ideas/algorithm.
    - Asymptotic Analysis is about measuring order of growth in terms of input size.
"""
"""
Order Of Growth
A function f(n) is said to be growing faster than g(n) if:
lim           g(n)/f(n) = 0
n->infinite

or

lim             f(n)/g(n) = infinite
n->infinite

f(n) and g(n) represent time taken.
n>=0
f(n),g(n) >= 0

Direct way to find, Find and compare growths
    - Ignore lower order terms
    - Ignore leading terms constants

Examples: 
    - f(n) = 2(n^2) + n + 6, Order of growth: n^2 (Quadratic)
    - g(n) = 100n, Order of growth: n (Linear)

How do we compare terms:
    - C < log(log(n)) < log(n) < n^(1/2) < n < n^2 < n^3 < n^4 < 2^n < n^n
"""

"""
BIG O Notation
    - We say f(n)=O(g(n)) if there exist constants C and n such that f(n) <= g(n) for all n>=no
    - f(n) <= g(n) for all n>=no

BIG OMEGA Notation
    - f(n) = Omega(g(n)) if there exist positive constants C and no such that 0 <= cg(n) <= f(n) for all n >= no
    - if f(n) = Omega(g(n)) then g(n) = O(f(n))
    - Omega notation is useful when we have lower band on time complexity

BIG THETA Notation
    - f(n) = theta(g(n)) if there exist constants C1, C2 (Where C1 > 0 and C2 > 0) and no (where no >= 0) such that c1(g(n)) <= f(n) <= c2(g(n)) for all n >= no
    - If f(n) = theta(g(n))
        then f(n) = O(g(n)) and f(n) = Omega(g(n))
        and g(n) = O(f(n)) and g(n) = Omega(f(n))
    - Represents Exact Bond
"""

"""
ANALYSIS OF ALGORITHM:

    Recursion Tree Method:
        - We write non-recursive part as root of tree and recursive parts as children.
        - We keep expanding children until we see a pattern.
"""
 
def fun_4(n):
    if n==1:
        return
    for i in range(n):
        print("GFG")
    fun_4(n/2)
    fun_4(n/2)

