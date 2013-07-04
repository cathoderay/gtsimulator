import random

from util import helper
from util.color import Color


class World:
    def __init__(self, dimension):
        self.dimension = dimension
        self.time = 0
        self.creatures = []
        self.feeds = []

    def random_populate(self, number_of_creatures):
        for i in range(number_of_creatures):
            x = random.choice(range(20, self.dimension[0]-20))
            y = random.choice(range(20, self.dimension[1]-20))
            self.creatures.append(Creature(position=[x, y], 
                                           size=4,
                                           energy=1000, 
                                           color=[0, 255, 0],
                                           field=100))

    def random_cultivate(self, number_of_feeds):
        for i in range(number_of_feeds):
            x = random.choice(range(0, self.dimension[0]))
            y = random.choice(range(0, self.dimension[1]))
            self.feeds.append(Feed(position=[x, y], 
                                   size=3, 
                                   energy=50, 
                                   color=Color.brown))
       
    def increase_time(self):
        self.time += 1


class Creature:
    def __init__(self, position, size, energy, color, field):
        self.position = position
        self.size = size
        self.energy = energy
        self.max_energy = energy
        self.color = color
        self.field = field      
        self.last_direction = self.random_direction()  

    def is_hungry(self):
        return self.energy < self.max_energy/2.0

    def is_dead(self):
        return self.energy <= 0 
           
    def eat(self, feed):
        self.increase_energy(feed.energy)
        if not self.is_hungry():
            self.change_color(Color.green)
    
    def walk_to(self, dimension, direction):
        new_position = helper.add_direction(self.position, direction)
        if helper.valid_position(dimension, self.position, self.size):
            self.position = new_position
            self.last_direction = direction
            self.reduce_energy(1)

    def walk(self, dimension):
        direction = self.last_direction
        if random.random() < 0.01:
            direction = self.random_direction()
        new_position = helper.add_direction(self.position, direction)
        if helper.valid_position(dimension, new_position, self.size):
            self.position = new_position
            self.last_direction = direction
            self.reduce_energy(1)
        else:
            self.last_direction = self.random_direction()
    
    def increase_energy(self, amount):
        self.energy += amount

    def reduce_energy(self, amount):
        self.energy -= amount

    def change_color(self, color):
        self.color = color

    def add_direction(v1, v2, method=helper.add_direction):
        return method(v1, v2)

    def random_direction(self, method=helper.choose_direction):
        return method()

    def reach_feed(self, feed, method=helper.reach_feed):
        return method(self, feed)

    def calculate_closer_feed(self, feeds, method=helper.calculate_closer_feed):
        return method(self, feeds)
    
    def calculate_direction(self, target, method=helper.calculate_direction):
        return method(self, target)

    def look_for_feed(self, feeds, method=helper.look_for_feed):
        return method(self, feeds)


class Feed:
    def __init__(self, position, size, energy, color):
        self.position = position
        self.size = size
        self.energy = energy
        self.color = color
