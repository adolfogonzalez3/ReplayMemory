
import random
from collections import deque
from ReplayMemory.Replay import Replay

class SimpleReplay(Replay):
    def __init__(self, size=5000):
        self.memory = deque(maxlen=size)
        
    def insert(self, data):
        self.memory.append(data)
        
    def batch(self, K=32):
        return random.sample(self.memory, K)