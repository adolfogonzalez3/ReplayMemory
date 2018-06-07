
from ReplayMemory.Replay import Replay
from ReplayMemory.SumTree import SumTree

class PrioritizedReplay(Replay):
    def __init__(self, size=32):
        self.size = size
        self.memory = SumTree(size)
        
    def insert(self, data, weight):
        self.memory.insert(data, weight)

    def batch(self, K=32):
        return [self.memory.choose() for _ in range(K)]