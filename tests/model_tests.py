import unittest 

from model import *


class World_init(unittest.TestCase):
    def test_dimension(self):        
        world = World(dimension=(500, 400))
        self.assertEqual(world.dimension, (500, 400))

    def test_time_equal_0(self):
        world = World(dimension=(500, 400))
        self.assertEqual(world.time, 0)

    def test_no_creatures(self):
        world = World(dimension=(500, 400))
        self.assertEqual(len(world.creatures), 0)

    def test_no_feeds(self):
        world = World(dimension=(500, 400))
        self.assertEqual(len(world.feeds), 0)


class World_behavior(unittest.TestCase):
    def test_increase_time(self):
        world = World(dimension=(500, 400))
        before = world.time
        world.increase_time()
        after = world.time
        self.assertEqual(after, before + 1)


class Creature_init(unittest.TestCase):
    def test_size(self):
        creature = Creature(position=[2, 3], size=10, energy=5, color=[0, 255, 0], field=5)
        self.assertEqual(creature.size, 10)

    def test_energy(self):
        creature = Creature(position=[1, 3], size=10, energy=5, color=[0, 255, 0], field=5)
        self.assertEqual(creature.energy, 5)

    def test_color(self):
        creature = Creature(position=[2, 3], size=10, energy=5, color=[0, 255, 0], field=5)
        self.assertEqual(creature.color, [0, 255, 0])

    def test_position(self):
        creature = Creature(position=[1, 10], size=10, energy=5, color=[0, 255, 0], field=5)
        self.assertEqual(creature.position, [1, 10])

    def test_field(self):
        creature = Creature(position=[2, 3], size=10, energy=5, color=[0, 255, 0], field=5)
        self.assertEqual(creature.field, 5)

    def test_max_energy(self):
        creature = Creature(position=[2, 3], size=10, energy=5, color=[0, 255, 0], field=5)
        self.assertEqual(creature.max_energy, 5)


class Creature_behavior(unittest.TestCase):
    def test_hungry(self):
        creature = Creature(position=[2, 3], size=10, energy=10, color=[0, 255, 0], field=5)
        creature.energy = 2
        hungry = creature.is_hungry()
        self.assertEqual(hungry, True)

    def test_death(self):
        creature = Creature(position=[2, 3], size=10, energy=0, color=[0, 255, 0], field=5)
        self.assertEqual(creature.is_dead(), True) 

    def test_death_negative_energy(self):
        creature = Creature(position=[2, 3], size=10, energy=-2, color=[0, 255, 0], field=5)
        self.assertEqual(creature.is_dead(), True) 

    def test_increase_energy(self):
        creature = Creature(position=[2, 3], size=10, energy=10, color=[0, 255, 0], field=4)
        creature.increase_energy(8)
        self.assertEqual(creature.energy, 18)

    def test_reduce_energy(self):
        creature = Creature(position=[2, 3], size=10, energy=10, color=[0, 255, 0], field=4)
        creature.increase_energy(-8)
        self.assertEqual(creature.energy, 2)

    def test_change_color(self):
        creature = Creature(position=[2, 3], size=10, energy=5, color=[0, 255, 0], field=2)
        creature.change_color([1, 1, 0])
        self.assertEqual(creature.color, [1, 1, 0])

    def test_look_for_feeds_1_collisions(self):
        creature = Creature(position=[3, 4], size=3, energy=10, color=[0, 255, 0], field=2)
        feeds = []
        feed = Feed(position=[7, 7], size=3, energy=10, color=Color.brown)
        feeds.append(feed)
        feeds_found = creature.look_for_feed(feeds)
        self.assertEqual(len(feeds_found), 1)

    def test_look_for_feeds_2_collisions(self):
        creature = Creature(position=[3, 4], size=3, energy=10, color=[0, 255, 0], field=4)
        feeds = []
        feed1 = Feed(position=[7, 7], size=3, energy=10, color=Color.brown)
        feeds.append(feed1)
        feed2 = Feed(position=[3, 10], size=3, energy=10, color=Color.brown)
        feeds.append(feed2)
        feeds_found = creature.look_for_feed(feeds)
        self.assertEqual(len(feeds_found), 2)

    def test_look_for_feeds_0_collisions(self):
        creature = Creature(position=[3, 4], size=3, energy=10, color=[0, 255, 0], field=4)
        feeds = []
        feed = Feed(position=[50, 50], size=3, energy=10, color=Color.brown)
        feeds.append(feed)
        feeds_found = creature.look_for_feed(feeds)
        self.assertEqual(len(feeds_found), 0)

    def test_calculate_closer_feed(self):
        creature = Creature(position=[3, 4], size=1, energy=10, color=[0, 255, 0], field=4)
        feeds = []
        feed1 = Feed(position=[7, 8], size=1, energy=10, color=Color.brown)
        feed2 = Feed(position=[7, 7], size=1, energy=10, color=Color.brown)
        feeds.append(feed1)
        feeds.append(feed2)
        closer_feed = creature.calculate_closer_feed(feeds)
        self.assertEqual(closer_feed.position, [7, 7])

    def test_reach_feed_1(self):
        creature = Creature(position=[3, 4], size=3, energy=10, color=[0, 255, 0], field=4)
        feed = Feed(position=[5, 6], size=3, energy=10, color=Color.brown)
        self.assertEqual(creature.reach_feed(feed), True)

    def test_reach_feed_2(self):
        creature = Creature(position=[5, 4], size=3, energy=10, color=[0, 255, 0], field=2)
        feed = Feed(position=[9, 7], size=7, energy=10, color=Color.brown)
        self.assertEqual(creature.reach_feed(feed), True)

    def test_walk_down(self):
        creature = Creature(position=[3, 4], size=3, energy=10, color=[0, 255, 0], field=4)
        creature.walk_to([800, 600], [0, 1])
        self.assertEqual(creature.position, [3, 5])

    def test_walk_up(self):
        creature = Creature(position=[3, 4], size=3, energy=10, color=[0, 255, 0], field=4)
        creature.walk_to([800, 600], [0, -1])
        self.assertEqual(creature.position, [3, 3])

    def test_walk_left(self):
        creature = Creature(position=[3, 4], size=3, energy=10, color=[0, 255, 0], field=4)
        creature.walk_to([800, 600], [-1, 0])
        self.assertEqual(creature.position, [2, 4])

    def test_walk_right(self):
        creature = Creature(position=[3, 4], size=3, energy=10, color=[0, 255, 0], field=4)
        creature.walk_to([800, 600], [1, 0])
        self.assertEqual(creature.position, [4, 4])

    def test_calculate_direction(self):
        creature = Creature(position=[3, 4], size=3, energy=10, color=[0, 255, 0], field=4)
        feed = Feed(position=[1, 1], size=10, energy=10, color=Color.brown)
        direction = creature.calculate_direction(feed)
        self.assertNotEqual(direction, [1, 1])
        self.assertNotEqual(direction, [-1, 1])
        self.assertNotEqual(direction, [1, -1])        
        self.assertNotEqual(direction, [-1, -1])                
        

class Feed_init(unittest.TestCase):
    def test_energy(self):
        feed = Feed(position=[1, 1], size=10, energy=10, color=Color.brown)
        self.assertEqual(feed.energy, 10)

    def test_size(self):
        feed = Feed(position=[1, 1], size=10, energy=7, color=Color.brown)
        self.assertEqual(feed.size, 10)

    def test_position(self):
        feed = Feed(position=[1, 1], size=10, energy=7, color=Color.brown)
        self.assertEqual(feed.position, [1, 1])

    def test_color(self):
        feed = Feed(position=[1, 1], size=10, energy=7, color=Color.brown)
        self.assertEqual(feed.color, Color.brown)
       

if __name__ == "__main__":
    unittest.main()
