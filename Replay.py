
from abc import ABC, abstractmethod

class Replay(ABC):        
    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def batch(self, K=32):
        pass