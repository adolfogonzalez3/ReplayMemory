
import random

#from ReplayMemory.Replay import Replay
#from ReplayMemory.SumTree import SumTree

from ReplayMemory.SimpleReplay import SimpleReplay

from collections import deque

class PrioritizedReplay(SimpleReplay):
    def __init__(self, max_size=5000, on_disk=False):
        super().__init__(max_size, on_disk)
        self.weights = deque(maxlen=max_size)
        
    def insert(self, data, weight):
        #self.memory.insert(data, weight)
        #self.memory.append(data)
        super().insert(data)
        self.weights.append(weight)

    def batch(self, K=32):
        #return [self.memory.choose() for _ in range(K)]
        return random.choices(self, weights=self.weights, k=K)
        