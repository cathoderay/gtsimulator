import random


class Element:
    def __init__(self, center, size):
        """Basic element of the world.
        Size zero is the special case where the element is a pixel."""
        self.center = center
        self.centerx = center[0]
        self.centery = center[1]
        self.left = center[0] - size
        self.right = center[0] + size
        self.top = center[1] - size
        self.bottom = center[1] + size
     
    def distance(self, e):
        """Return Manhattam distance between 2 elements."""
        distance = 0
        correction = 0           
        if e.left > self.right:
            distance += e.left - self.right - 1
            correction += 1
        if e.right < self.left:
            distance +=  self.left - e.right - 1
            correction += 1
        if e.top > self.bottom:
            distance += e.top - self.bottom - 1
            correction += 1
        if e.bottom < self.top:
            distance +=  self.top - e.bottom - 1
            correction += 1        
        
        if correction == 2:
            distance += 1
    
        #case where it collides
        if correction == 0:
            return -1
        return distance

    def direction_to(self, e):
        """Return a valid direction to another Element"""
        delta_x = delta_y = 0
        if self.right < e.left:
            delta_x += 1
        if e.right < self.left:
            delta_x -= 1
        if self.top > e.bottom:
            delta_y -= 1
        if self.bottom < e.top:
            delta_y += 1
        
        if delta_y != 0 and delta_x != 0:
            return random.choice([[delta_x, 0], [0, delta_y]])
        return [delta_x, delta_y]
            
    def collide(self, e):
        """Check for colllision between 2 Elements"""
        if self.distance(e) < 0:
            return True
        return False


class Vector:
    @classmethod
    def random_direction(cls):
        """Return a valid direction randomly"""
        return random.choice([[1, 0], [0, 1], [-1, 0], [0, -1] ])

    @classmethod
    def add(cls, v1, v2):
        """Return the sum of 2 vectors"""
        return [v1[0] + v2[0], v1[1] + v2[1]]
