"""
TRIE DATA STRUCTURE ADVANCE
"""
from collections import defaultdict
"""
Introduction:
    - Efficient for the following operations on words in a dictionary.
        = Search
        = Insert 
        = Delete
        = Prefix Search
        = Lexicographical Ordering of a Work
    
    - Time Complexities based on Operations
        = Search : theta(word_length)
        = Insert : theta(word_length)
        = Delete : theta(word_length)
        = Prefix_Search : theta(prefix_length+output_length)
        = Lexicographic_Ordering : theta(output_length)
"""

"""
Trie Representation:
    code:
        class TrieNode:
            child = [None]*26
            is_end_of_word = False
"""

"""
- Insert and Search in Trie Data Structure

- Deletion in Trie Data Structure
    Idea:
        - We wite a recursive function
        - We first traverse to the last node; we mark it not end of a word
        - if this node is empty(Contains 0 children), We remove it
        - if parent of this node had only one child and not end of a word, we remove parent as well.
        - We repeat the above step for parent of parent and so on.
"""
from os import remove
from tkinter import S


class TrieNode:
    def __init__(self):
        self.children =[None]*26
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = self.getNode()
    
    def getNode(self):
        return TrieNode()
    
    def _charToIndex(self,ch):
        return ord(ch)-ord('a')
    
    def insert(self,key):
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            if not p_crawl.children[index]: # type: ignore
                p_crawl.children[index] = self.getNode() # type: ignore
            p_crawl= p_crawl.children[index] # type: ignore
        p_crawl.is_end_of_word =True # type: ignore
    
    
    def search(self,key):
        p_crawl = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])
            if not p_crawl.children[index]: # type: ignore
                return False 
            p_crawl = p_crawl.children[index] # type: ignore 
        return p_crawl.is_end_of_word # type: ignore
    
    def isEmpty(self):
        for x in self.root.children: # type: ignore
            if x!=None:
                return False
        return True
    
    def delete_Node(self,key,i=0):
        if self.root == None:
            return None
        if i == len(key):
            if self.root.is_end_of_word:
                self.root.is_end_of_word=False
            if self.isEmpty():
                self.root = None
            return self.root
        index = ord[key[i]] - ord('a') # type: ignore
        self.root.children[index] = remove(self.root.children[index],key,i+1) # type: ignore
        if self.isEmpty() and self.root.is_end_of_word == False:
            self.root = None
        return self.root
    
    

trie_keys=["the","a","there","anaswe","any","by","their"]
output = ["Not present in trie","Present in trie"]
t=Trie()
for key in trie_keys:
    t.insert(key)
print("{} ---- {}".format("the",output[t.search("the")]))
print("{} ---- {}".format("these",output[t.search("these")]))
print("{} ---- {}".format("their",output[t.search("their")]))
print("{} ---- {}".format("thaw",output[t.search("thaw")]))
print()

"""
Count Distinct Rows in Binary Matrix
"""
def unique_rows(arr):
    mp = defaultdict(int)
    t = ""
    
    for x in arr:
        t = ""
        for y in x:
            t+=y
        mp[t] += 1

    cnt = 0
    for x in mp:
        if(mp[x] == 1):
            cnt+=1
    return cnt
binary_matrix = [['0','1','1','0'],['0','1','1','1'],['0','1','1','0'],['0','1','0','0']]
print("Count Distinct Rows in Binary Matrix : ",unique_rows(binary_matrix))
