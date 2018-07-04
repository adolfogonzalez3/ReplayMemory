
from abc import ABC, abstractmethod

class Replay(ABC):

    def append(self, *args, **kwargs):
        self.insert(*args, **kwargs)
       
    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def batch(self, K=32):
        pass