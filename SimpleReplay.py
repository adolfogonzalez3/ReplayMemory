import numpy as np
import random
from collections import deque
from ReplayMemory.Replay import Replay

from DiskList import ArrayQueue

class SimpleReplay(Replay):
    def __init__(self, max_size=5000, on_disk=False):
        self.memory = []
        self.on_disk = on_disk
        self.types = None
        self.max_size = max_size
        self.current_size = 0
    
    def insert(self, data):
        if self.on_disk is True:
            self.__insert_on_disk(data)
        else:
            self.__insert_in_mem(data)
            
        
    def __insert_on_disk(self, data):
        if self.types is None:
            self.types = []
            for d in data:
                if type(d) is np.ndarray:
                    shape = d.shape
                    dtype = d.dtype
                    Q = ArrayQueue(max_size=self.max_size, shape=shape, dtype=dtype)
                    self.memory.append(Q)
                    
                else:
                    self.memory.append(deque(maxlen=self.max_size))
                self.types.append(type(d))
        for Q, d in zip(self.memory, data):
            Q.append(d)
            self.current_size = len(Q)
            
    def __insert_in_mem(self, data):
        self.memory.append(data)
        self.current_size = len(self.memory)
        
    def batch(self, K=32):
        try:
            if self.on_disk is True:
                return self.__batch_on_disk(K=K)
            else:
                return self.__batch_in_mem(K=K)
        except ValueError:
            raise ValueError(('Tried to sample {!s} experiences from '
                                'replay memory with current experience '
                                'size {!s}.').format(K, self.current_size))
        
    def __batch_on_disk(self, K):
        batch = []
        indices = random.sample(range(self.current_size), k=K)
        for index in indices:
            single = []
            for Q in self.memory:
                single.append(Q[index])
            batch.append(single)
        return batch
            
    def __batch_in_mem(self, K):
        return random.sample(self.memory, k=K)
        
    def __getitem_on_disk(self, key):
        item = []
        for Q in self.memory:
            item.append(Q[key])
        return item
        
    def __getitem_in_mem(self, key):
        return self.memory[key]
        
    def __len__(self):
        return self.current_size
        
    def __getitem__(self, key):
        if self.on_disk is True:
            return self.__getitem_on_disk(key)
        else:
            return self.__getitem_in_mem(key)