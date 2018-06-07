import numpy as np
import math, random
from enum import Enum, auto

class insertEnum(Enum):
    Insert = auto()
    ReplaceMin = auto()

class SumTree(object):
    def __init__(self, size=32):
        self.height = math.ceil(math.log2(size))
        self.weights = [0]*(2**(self.height+1) - 1)
        self.items = []
        self.size = size
        self.counter = 0
        
    def get_layer(self, d):
        start = 2**d - 1
        end = start + 2**d
        return (start, end)
    
    def find_min(self):
        index = 0
        left = index*2+1
        right = index*2+2
        start, end = self.get_layer(self.height)
        while index < start:
            if self.weights[left] > self.weights[right]:
                index = right
            else:
                index = left
            left = index*2+1
            right = index*2+2
        return index
    
    def bubbleup(self, index):
        if index%2 == 0:
            sibling = index - 1
            parent = int(index/2) - 1
        else:
            sibling = index + 1
            parent = int(sibling/2) - 1
        while parent > -1:
            self.weights[parent] = self.weights[index] + self.weights[sibling]
            index = parent
            if index%2 == 0:
                sibling = index - 1
                parent = int(index/2) - 1
            else:
                sibling = index + 1
                parent = int(sibling/2) - 1
    
    def insert(self, item, weight):
        length = len(self.items)
        start, end = self.get_layer(self.height)
        if length == self.size:
            #index = self.find_min()
            index = self.counter
            self.counter = (self.counter+1)%self.size
            self.weights[start+index] = weight
            self.items[index] = item
            self.bubbleup(start+index)
            return insertEnum.ReplaceMin
        else:
            self.items.append(item)
            self.weights[start+length] = weight
            self.bubbleup(start+length)
            return insertEnum.Insert
      
    def choose(self):
        index = 0
        left = index*2+1
        right = index*2+2
        start, end = self.get_layer(self.height)
        while index < start:
            L = self.weights[left]
            R = self.weights[right]
            if random.random() > L/(L+R):
                index = right
            else:
                index = left
            left = index*2+1
            right = index*2+2
        return self.items[index-start]