import unittest
import numpy as np

from ReplayMemory.SumTree import SumTree, insertEnum

class TestSumTree(unittest.TestCase):

    def test_insert(self):
        tree = SumTree(16)
        for i in range(16):
            with self.subTest(i=i):
                action = tree.insert(i, i)
                self.assertEqual(action, insertEnum.Insert)

    def test_replace(self):
        tree = SumTree(16)
        for i in range(16):
            action = tree.insert(i, i)
        for i in range(64):
            with self.subTest(i=i):
                action = tree.insert(i, i+16)
                self.assertEqual(action, insertEnum.ReplaceMin)
                
    def test_probability(self):
        tree = SumTree(4)
        for i in range(1, 5):
            action = tree.insert(i, i)
        counts = [0]*4
        RUNS = 10**6
        for i in range(RUNS):
            c = tree.choose()
            counts[c-1] += 1
        counts = [c/RUNS for c in counts]
        for i in range(4):
            with self.subTest(i=(i+1)):
                self.assertTrue(np.isclose(counts[i], (i+1)/10., rtol=1e-2))

if __name__ == '__main__':
    unittest.main()