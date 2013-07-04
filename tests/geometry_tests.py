import unittest

from geometry import *

class Geometry_init(unittest.TestCase):
    def test_center(self):
        e = Element(center=[1, 0], size=2)
        self.assertEqual(e.center, [1, 0])
        
    def test_centerx(self):
        e = Element(center=[1, 0], size=2)
        self.assertEqual(e.centerx, 1)

    def test_centery(self):
        e = Element(center=[1, 0], size=2)
        self.assertEqual(e.centery, 0)
        
    def test_left(self):
        e = Element(center=[1, 0], size=2)
        self.assertEqual(e.left, -1)

    def test_right(self):
        e = Element(center=[1, 0], size=2)
        self.assertEqual(e.right, 3)

    def test_top(self):
        e = Element(center=[1, 0], size=2)
        self.assertEqual(e.top, -2)

    def test_bottom(self):
        e = Element(center=[1, 0], size=2)
        self.assertEqual(e.bottom, 2)

class Geometry_distance(unittest.TestCase):
    def test_distance1(self):
        e1 = Element(center=[2, 5], size=1)
        e2 = Element(center=[10, 6], size=3)
        distance = e1.distance(e2)
        self.assertEqual(distance, 3)
            
    def test_distance2(self):
        e1 = Element(center=[2, 5], size=1)
        e2 = Element(center=[5, 5], size=1)
        distance = e1.distance(e2)
        self.assertEqual(distance, 0)

    def test_distance3(self):
        e1 = Element(center=[6, 1], size=1)
        e2 = Element(center=[2, 5], size=1)
        distance = e1.distance(e2)
        self.assertEqual(distance, 3)

    def test_distance4(self):
        e1 = Element(center=[2, 12], size=1)
        e2 = Element(center=[2, 5], size=1)
        distance = e1.distance(e2)
        self.assertEqual(distance, 4)

    def test_collide5(self):
        e1 = Element(center=[3, 8], size=0)
        e2 = Element(center=[9, 3], size=0)
        distance = e1.distance(e2)        
        self.assertEqual(distance, 10)


class Geometry_collide(unittest.TestCase):
    def test_collide1(self):
        e1 = Element(center=[2, 2], size=1)
        e2 = Element(center=[2, 3], size=1)
        self.assertEqual(e1.collide(e2), True)
        
    def test_collide2(self):
        e1 = Element(center=[10, 6], size=3)
        e2 = Element(center=[2, 5], size=1)
        self.assertEqual(e1.collide(e2), False)
        
    def test_collide3(self):
        e1 = Element(center=[2, 2], size=1)
        e2 = Element(center=[5, 2], size=1)
        self.assertEqual(e1.collide(e2), False)

    def test_collide4(self):
        e1 = Element(center=[3, 8], size=0)
        e2 = Element(center=[9, 3], size=0)
        self.assertEqual(e1.collide(e2), False)

class Geometry_direction_to(unittest.TestCase):
    def test_direction(self):
        e1 = Element(center=[6, 3], size=1)
        e2 = Element(center=[3, 6], size=1)
        direction = e1.direction_to(e2)
        self.assertEqual(direction[0] == 0 or direction[1] == 0, True)
        
    
if __name__ == "__main__":
    unittest.main()
