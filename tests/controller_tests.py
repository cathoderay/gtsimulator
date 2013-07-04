import unittest 

from controller import *

class Simulator_init(unittest.TestCase):
    def test_world_dimension(self):
        simulator = Simulator(world_dimension=(1, 2))
        self.assertEqual(simulator.dimension, (1, 2))


if __name__ == '__main__':
    unittest.main()
