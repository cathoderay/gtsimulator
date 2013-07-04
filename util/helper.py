import random

import geometry


def valid_position(dimension, position, size):
    e = geometry.Element(position, size)
    if e.left < 0:
        return False
    elif e.right >= dimension[0]:
        return False
    elif e.top < 0:
        return False
    elif e.bottom >= dimension[1]:
        return False
    return True


def look_for_feed(creature, feeds):
    """Return the feeds that the creatures can feel around"""
    feeds_found = []
    e1 = geometry.Element(creature.position, creature.size+creature.field)
    for feed in feeds:
        e2 = geometry.Element(feed.position, feed.size)
        if e1.collide(e2):
            feeds_found.append(feed)
    return feeds_found


def calculate_closer_feed(creature, feeds):
    """Return the closer feed"""
    minimum = 10000000000000000000
    e1 = geometry.Element(creature.position, creature.size)
    for feed in feeds:
        e2 = geometry.Element(feed.position, feed.size)
        distance = e1.distance(e2)
        if distance < minimum:
            minimum = distance
            closer_feed = feed
    return closer_feed


def calculate_direction(creature, target):
    """Calculate the unitary direction to a target"""
    e1 = geometry.Element(creature.position, creature.size)
    e2 = geometry.Element(target.position, target.size)    
    direction = e1.direction_to(e2)    
    return direction

    
def reach_feed(creature, feed):
    """Return if the creature collides with the feed, that is, ready to eat"""
    e1 = geometry.Element(creature.position, creature.size)
    e2 = geometry.Element(feed.position, feed.size)
    return e1.collide(e2)


def add_direction(vector1, vector2):
    """Add vectors"""
    return geometry.Vector.add(vector1, vector2)

        
def choose_direction():
    """Return a direction"""
    return geometry.Vector.random_direction()
