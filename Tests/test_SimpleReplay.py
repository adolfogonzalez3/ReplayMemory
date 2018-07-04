import unittest
import numpy as np

from ReplayMemory import SimpleReplay

def build_test_experience(i):
    a = i
    b = np.empty((10, 15))
    b.fill(i)
    c = np.empty((10, 5, 10))
    c.fill(i)
    d = i%2 == 0
    e = [i for _ in range(10)]
    return (a, b, c, d, e)
    
    

class TestSimpleReplay(unittest.TestCase):

    def test_insert_on_disk(self):
        replay = SimpleReplay(on_disk=True)
        experience = build_test_experience(0)
        replay.append(experience)
        
    def test_insert_in_mem(self):
        replay = SimpleReplay(on_disk=False)
        experience = build_test_experience(0)
        replay.append(experience)
        
    def test_batch_on_disk(self):
        replay = SimpleReplay(on_disk=True)
        for _ in range(32):
            experience = build_test_experience(0)
            replay.append(experience)
            
        experiences = replay.batch(1)[0]
        a, b, c, d, e = experiences
        self.assertEqual(b.shape, (10, 15))
        self.assertEqual(c.shape, (10, 5, 10))
        self.assertEqual(len(e), 10)
        
    def test_batch_in_mem(self):
        replay = SimpleReplay(on_disk=False)
        for _ in range(32):
            experience = build_test_experience(0)
            replay.append(experience)
            
        experiences = replay.batch(1)[0]
        a, b, c, d, e = experiences
        self.assertEqual(b.shape, (10, 15))
        self.assertEqual(c.shape, (10, 5, 10))
        self.assertEqual(len(e), 10)
        
    def test_batch_on_disk_exception(self):
        replay = SimpleReplay(on_disk=True)
        for _ in range(32):
            experience = build_test_experience(0)
            replay.append(experience)
            
        with self.assertRaises(ValueError):
            replay.batch(64)
            
        def test_batch_on_disk_exception(self):
            replay = SimpleReplay(on_disk=False)
            for _ in range(32):
                experience = build_test_experience(0)
                replay.append(experience)
                
            with self.assertRaises(ValueError):
                replay.batch(64)

if __name__ == '__main__':
    unittest.main()