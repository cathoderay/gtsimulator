from util import file
from model import *


class Simulator:
    """Simulator take care of a world
    If a file is passed, a world is created from it.
    """
    def __init__(self, file_path=None, world_dimension=(800, 600)):        
        if file_path:
            self.world = file.open_world(file_path)
        else:
            self.dimension = world_dimension
            self.world = World(self.dimension)
            self.world.random_populate(10)
            self.world.random_cultivate(300)
         
    def step(self):
        """The world advance a step"""
        feeds = self.world.feeds
        creatures = self.world.creatures
        for creature in creatures:
            if creature.is_dead():
                creatures.remove(creature)
            elif creature.is_hungry():
                creature.change_color(Color.red)
                feeds_found = creature.look_for_feed(feeds)
                if len(feeds_found) > 0:
                    closer_feed = creature.calculate_closer_feed(feeds_found)
                    if creature.reach_feed(closer_feed):
                        creature.eat(closer_feed)
                        feeds.remove(closer_feed)
                    else:
                        direction = creature.calculate_direction(closer_feed)
                        creature.walk_to(self.world.dimension, direction)
                else:
                    creature.walk(self.world.dimension)
            creature.reduce_energy(1)

        if self.world.time % 20 == 0:
            self.world.random_cultivate(20)
        self.world.increase_time()

    def get_world(self):
        """Return the world's state"""
        return self.world
