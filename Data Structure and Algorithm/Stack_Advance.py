"""
STACK ADVANCE CONCEPTS AND QUESTIONS
"""

"""
Concept - 1: Implement two stacks in an Array 

    Brute Force:
        - We divide the array from middle
            = We use first half for stack_1 and second half for stack_2
        - Inefficient use of space
            = if we add 5 items to stack_1, and no items to stack_2, then we cannot add more items to stack_1 even if we have space in the array
    
    Efficient Solution: 
        - Begin both stacks from the two corners of the array
        - Now  we can insert items in any stack as long as we have space.
"""
class TwoStacks:
    def __init__(self,n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size
    
    def push_1(self,x):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
            return True
        return False
    
    def push_2(self,x):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x
            return True
        return False
    
    def pop_1(self):
        if self.top1>=0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        return None
    
    def pop_2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        return None
    
    def size_1(self):
        return self.top1 + 1
    
    def size_2(self):
        return self.size - self.top2
print("Concept of Two Stacks in an Array")
two_stacks = TwoStacks(5)
two_stacks.push_1(10)
two_stacks.push_2(20)
print("First Element of Stack 1: ",two_stacks.pop_1())
print()

"""
Concept - 2 : Implement K stacks in an Array
"""
class KStacks:
    def __init__(self,n,k):
        self.cap = n
        self.k = k
        self.arr = [None] * n
        self.top = [-1] * k
        self.next = [i+1 for i in range(n)]
        self.next[n-1] = -1
        self.free_top = 0
    
    def push(self,sn,x):
        i = self.free_top
        self.free_top = self.next[self.free_top]
        self.arr[i] = x
        self.next[i] = self.top[sn]
        self.top[sn] = i
    
    def pop(self,sn):
        prev_top = self.top[sn]
        self.top[sn] = self.next[prev_top]
        self.next[prev_top] = self.free_top
        self.free_top = prev_top
        return self.arr[prev_top]
    
    def isEmpty(self,sn):
        return self.top[sn] == -1


"""
Problem Statement: Stock span problem
"""
def stock_span_problem_1(arr):
    res = []
    for i in range(len(arr)):
        span = 1
        j = i-1
        while j>=0 and arr[i] >= arr[j]:
            span += 1
            j -= 1
        res.append(span)
    return res
print("Stock span problem (Naive) O(n^2): ",stock_span_problem_1([18,12,13,14]))
"""
Observation: 
=> If there is a greatest element on left side;
Span = (Index of Current Element) - (Index of Closest Greater Element on Left Side)
=> Otherwise;
Span = Index of current element + 1


"""
def stock_span_problem_2(arr):
    st = []
    res = []
    st.append(0)
    res.append(1)
    for i in range(1,len(arr)):
        while len(st)>=0 and arr[st[-1]]<=arr[i]:
            st.pop()
        span = (i+1) if len(st) == 0 else i-st[-1]
        res.append(span)
        st.append(i)
    return res
print("Stock span problem (Efficient): ",stock_span_problem_2([60,10,20,15,35,50]))
print()

"""
Problem Statement: Previous Greater element
"""
def previous_greater_element_1(arr):
    res = []
    for i in range(len(arr)):
        pg = -1
        for j in range(i-1,-1,-1):
            if arr[j]>arr[i]:
                pg = arr[j]
                break
        res.append(pg)
    return res
print("Previous greater element (Naive) O(n^2): ",previous_greater_element_1([20,30,10,5,15]))
def previous_greater_element_2(arr):
    res = []
    st = []
    for i in range(len(arr)):
        while len(st)>0 and st[-1]<=arr[i]:
            st.pop()
        pg = -1 if len(st) == 0 else st[-1]
        res.append(pg)
        st.append(arr[i])
    return res
print("Previous greater element (Efficient) O(n): ",previous_greater_element_2([20,30,10,5,15]))
print()

"""
Problem Statement : Next Greater Element
"""
def next_greater_element_1(arr):
    res = []
    for i in range(len(arr)):
        ng = -1
        for j in range(i+1,len(arr)):
            if arr[j] > arr[i]:
                ng = arr[j]
                break
        res.append(ng)
    return res
print("Next greater element (Naive) O(n^2): ",next_greater_element_1([5,15,10,8,6,12,7]))
def next_greater_element_2(arr):
    res = [None] * len(arr)
    st = []
    for i in range(len(arr)-1,-1,-1):
        while len(st)>0 and st[-1]<=arr[i]:
            st.pop()
        res[i] = -1 if len(st) == 0 else st[-1] # type: ignore
        st.append(arr[i])
    return res
print("Next greater element (Efficient) O(n): ",next_greater_element_2([5,15,10,8,6,12,7]))
print()

"""
Problem Statement: Largest Rectangular area in a histogram
"""
def largest_rectangular_area_histogram_1(arr):
    res = 0
    for i in range(len(arr)):
        curr = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>=arr[i]:
                curr+=arr[i]
            else:
                break
        for j in range(i+1,len(arr)):
            if arr[j] >= arr[i]:
                curr+=arr[i]
            else:
                break
        res = max(res,curr)
    return res
print("Largest area of rectangular histogram: ",largest_rectangular_area_histogram_1([6,2,5,4,1,5,6]))
"""
Efficient Solution:
    - Initialize : res = 0
    - Find Pervious smaller element for every element
    - Find Next smaller element for every element
    - Do following for every element arr[i]
        curr = arr[i]
        curr += (i - ps[i] - 1) * arr[i]
        curr += (ns[i] - i - 1) * arr[i]
        res = max(res,curr)
    - return res
"""
def largest_rectangular_area_histogram_2(arr):
    res = 0
    st = []
    for i in range(len(arr)):
        while st and arr[st[-1]] >= arr[i]:
            tp = st[-1]
            st.pop()
            curr_width = (i-st[-1]-1) if st else i
            res = max(res,curr_width * arr[tp])
        st.append(i)
    
    while st:
        tp = st[-1]
        st.pop()
        curr_width = (len(arr) - st[-1] -1 ) if st else len(arr)
        res = max(res,curr_width*arr[tp])
    return res
print("Largest area of rectangular histogram (Efficient): ",largest_rectangular_area_histogram_2([6,2,5,4,1,5,6]))
print()
"""
Problem Statement: Largest rectangle with all 1's
    Naive Solution:
        - Consider every cell as a straight point
        - Consider all sizes of rectangles with current cell as a straight point
        - For the current rectangle, check if it has all 1's. If yes,then update the res if the current size is more.
        - Time Complexity: O(R^3 * C^3)
    
    Efficient Solution:
        - Run a loop from 0 to R-1
            = Update the histogram for the current row
            = Find the largest area in the histogram and update the result if required
"""
def largest_rectangle_with_all_1s(arr):
    res = largest_rectangular_area_histogram_2(arr[0])
    for i in range(1,len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]:
                arr[i][j]+=arr[i-1][j]
        res = max(res,largest_rectangular_area_histogram_2(arr[i]))
    return res
print("Largest rectangle with all 1s O(R*C): ",largest_rectangle_with_all_1s([[1,0,0,1,1],[0,0,0,1,1],[1,1,1,1,1]])) 
print()

"""
Problem Statement: Design a stack that support normal stack operations in O(1) and also supports getMin() in O(1)
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return "Node({})".format(self.value)
    __repr__ = __str__

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None
    
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = "\n".join(out)
        return ("Top {} \n\nStack : \n".format(self.top,out))
    
    __repr__=__str__

    def getMin(self):
        if self.top is None:
            return "Stack is Empty"
        else:
            print("Minimum Element in the stack is: {}".format(self.minimum))
    
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count+=1
        return self.count
    
    def peek(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            if self.top.value < self.minimum:
                print("Top Most element is: {}".format(self.minimum))
            else:
                print("Top Most element is: {}".format(self.top.value))
    
    def push(self,value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value
        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top #type:ignore
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top # type: ignore
            self.top = new_node
        print("Number Inserted: {}".format(value))
    
    def pop(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print("Top most element removed: {}".format(self.minimum))
                self.minimum = ((2*self.minimum)- removedNode) # type: ignore
            else:
                print("Top most element removed: {}".format(removedNode))
print("A Stack that support normal stack operations in O(1) and also supports getMin() in O(1): ")
s = Stack()
s.push(3)
s.push(5)
s.getMin()
s.push(2)
s.push(1)
s.getMin()
s.pop()
s.getMin()
s.pop()
s.peek()
print()

"""
Infix, Postfix and Prefix Introduction
    - Infix : x + y
    - Postfix : xy+
    - Prefix : +xy

Advantages of Prefix and Postfix:
    - Do not require parenthesis, precedence rules and associativity rules
    - Can be evaluated by writing a program that traverse the given expression exactly one.
"""
class Conversion:
    def __init__(self,capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {"+":1,"-":1,"*":2,"/":2,"^":3}
    
    def isEmpty(self):
        return True if self.top == -1 else False
    
    def peek(self):
        return self.array[-1]
    
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    
    def push(self,op):
        self.top += 1
        self.array.append(op)
    
    def isOperand(self,ch):
        return ch.isalpha()
    
    def notGreater(self,i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a<=b else False
        except KeyError:
            return False
    
    def infixToPostfix(self,exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == "(":
                self.push(i)
            elif i == ")":
                while((not self.isEmpty())) and self.peek()!="(":
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek()!="("):
                    return -1
                else:
                    self.pop()
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        
        while not self.isEmpty():
            self.output.append(self.pop())
        
        print("".join(self.output))

print("Infix to Postfix Conversion (Efficient Method): ")
exp_1 = "a+b*(c^d-e)^(f+g*h)-i"
ob_1 = Conversion(len(exp_1))
ob_1.infixToPostfix(exp_1)
print()
"""
Efficient Algorithm to convert Infix To Postfix
    - Create an empty stack, st
    - Do following for every character x from left to right
    - if x is :
        = Operand : output it
        = Left Parenthesis : Push to st
        = Right Parenthesis: Pop from st until left parenthesis is found. Output the popped operator.
        = Operator : if st is empty, push x to st; else compare with st top
            - Higher precedence (than st top), push to st
            - Lower precedence, pop st top and output until a higher precedence operator is found. Then push s to st
            - Equal precedence, use associativity
    - P op and output everything from st
"""

"""
Problem Statement: Evaluation of postfix
    - Create an empty stack st.
    - Traverse through every symbol x of given postfix
        = If x in an operand, push to st
        = Else (x is an operator)
            - op1 = st.pop()
            - op2 = st.pop()
            - compute op2 x op1 and push the result to st
            - return s.top()
"""
class Evaluate:
    def __init__(self,capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
    
    def isEmpty(self):
        return True if self.top == -1 else False
    
    def peek(self):
        return self.array[-1]
    
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    
    def push(self,op):
        self.top+=1
        self.array.append(op)
    
    def evaluatePostfix(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push (str(eval(val2 + i + val1)))
        return int(self.pop())
exp_2 = "231*+9-"
obj_2 = Evaluate(len(exp_2))
print("Evaluation of Postfix expression: ",obj_2.evaluatePostfix(exp_2))
print()

"""
Problem Statement: Infix to Prefix using stack.
    Algorithm :
        - Create an Empty stack, st
        - Create an Empty string, prefix
        - Do following for every character c from right to left.
        - If C is:
            = Operand : Push it to prefix
            = Right Parenthesis : Push to st
            = Left Parenthesis : Pop from st until right parenthesis is found. Append the popped character to prefix.
        - Operator: if st is empty, push c to st else, compare with st top.
            = Higher Precedence(than st top) : push C to st.
            = Lower Precedence : Pop st top and append the popped item to prefix until a higher precedence operator is found (on st becomes empty). Push c to st.
            = Equal Precedence : Use associativity
        - Pop everything : 
"""
def isOperator(c):
    return (not(c>='a' and c<='z') and not(c>='0' and c<='9') and not(c>='A' and c<= 'Z'))

def getPriority(C):
    if C == '-' or C == "+":
        return 1
    elif C == "*" or C == "/":
        return 2
    elif C == "^":
        return 3
    return 0

def infixToPrefix(infix):
    operators = []
    operands = []

    for i in range(len(infix)):
        if infix[i] == "(":
            operators.append(infix[i])
        elif infix[i] == ")":
            while len(operators)!=0 and operators[-1]!= "(":
                op1 = operands[-1]
                operands.pop()

                op2 = operands[-1]
                operands.pop()

                op = operators[-1]
                operators.pop()
                
                tmp = op + op2 + op1
                operands.append(tmp)
            operators.pop()
        
        elif (not isOperator(infix[i])):
            operands.append(infix[i] + "")
        
        else:
            while len(operators)!=0 and getPriority(infix[i])<=getPriority(operators[-1]):
                op1 = operands[-1]
                operands.pop()
                
                op2 = operands[-1]
                operands.pop()
                
                op = operators[-1]
                operators.pop()
                
                tmp = op + op2 + op1
                operands.append(tmp)
            operators.append(infix[i])
    
    while len(operators)!=0:
        op1 = operands[-1]
        operands.pop()

        op2 = operands[-1]
        operands.pop()    
        
        op = operands[-1]
        operators.pop()
        
        tmp = op + op2 + op1
        operands.append(tmp)

    return operands[-1]
# print("Infix to Prefix (S): ",infixToPrefix("(A-B/C)*(A/K-L)"))

"""
Problem Statement: Evaluation of prefix
"""
def is_operand(c):
    return c.isdigit()

def evaluate_prefix(expression):
    stack = []
    for c in expression[::-1]:
        if is_operand(c):
            stack.append(int(c))
        else:
            o1 = stack.pop()
            o2 = stack.pop()
            if c == "+":
                stack.append(o1 + o2)
            elif c == "-":
                stack.append(o1-o2)
            elif c == "*":
                stack.append(o1*o2)
            elif c == "/":
                stack.append(o1/o2)
    return stack.pop()
print("Evaluation of Prefix Expression: ",evaluate_prefix("+9*26"))