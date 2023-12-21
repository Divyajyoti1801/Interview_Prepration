"""
CREATING DYNAMIC ARRAY IN SCRATCH

"""


class DynamicArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.size = 0

    def get(self, i):
        return self.arr[i]

    def insert(self, i, n):
        self.arr[i] = n

    def pushback(self, n):
        return

    def popback(self):
        return

    def resize(self):
        return

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity
