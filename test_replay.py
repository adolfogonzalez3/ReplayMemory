import numpy as np
import random
from ReplayMemory import PrioritizedReplay, SimpleReplay
from DiskList import ArrayQueue

from tqdm import trange

if __name__ == '__main__':
    a = np.random.rand(80, 80, 4)
    replay = PrioritizedReplay(1000, on_disk=True)
    Q = ArrayQueue(1000, a.shape, dtype=np.float)
    w = [np.random.rand() for _ in range(10000)]
    for i in trange(1000):
        replay.append((a,), abs(np.random.normal(0, 20)))
        #Q.append(a)1
        
    for i in trange(10000):
        batch = replay.batch()
        #random.choices(Q, weights=w, k=32)
        #batch=[]
        #for i in range(32):
        #    batch.append(Q[i])
        
    for Q in replay.memory:
        print(Q.misses)