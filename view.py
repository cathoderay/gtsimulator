import os
import sys

import pygame
from pygame.locals import *

import controller
from util.view_util import *


class Screen:
    def __init__(self, width, height, caption, file):
        pygame.init()
        pygame.font.init()
        self.width = width    
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.temp = pygame.Surface([width, height])
        self.file = file
        pygame.display.set_caption(caption)        

    def start(self):
        self.stopped = False
        self.simulator = controller.Simulator(file_path=self.file)
        self.main_loop()

    def main_loop(self):
        while True:
           self.check_input()
           if not self.stopped:
                self.simulator.step()
                self.clean()
                self.draw_images(self.simulator.get_world())
                self.draw_instructions()
                self.update()         

    def check_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()        
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.start()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.stopped = not self.stopped

    def clean(self):
        self.temp.fill([0,0,0])

    def draw_images(self, world):
        #draw feeds       
        for feed in world.feeds:
            surface = pygame.Surface([feed.size*2+1, feed.size*2+1])
            surface_rect = surface.get_rect()
            surface_rect.centerx = feed.position[0]
            surface_rect.centery = feed.position[1]
            surface.fill(feed.color)
            self.temp.blit(surface, surface_rect)

        #draw creatures        
        for creature in world.creatures:
            surface = pygame.Surface([creature.size*2+1, creature.size*2+1])
            surface_rect = surface.get_rect()
            surface_rect.centerx = creature.position[0]
            surface_rect.centery = creature.position[1]
            surface.fill(creature.color)
            draw_text('%s' % creature.energy, 10, 
                      self.temp, (creature.position[0]-8, \
                      creature.position[1]-20))
            self.temp.blit(surface, surface_rect)
        
        #draw world properties
        draw_text('world_dimension = %s' % str(world.dimension), 15, self.temp, (50, 50))                    
        draw_text('time = %s' % world.time, 15, self.temp, (50, 70))                    

    def draw_instructions(self):
        draw_text('GTSimulator', 20, self.temp, (50, 30))             
        draw_text("Press 'R' to restart", 13, self.temp, (self.width - 150, 30))
        draw_text("Press 'P' to stop/play", 13, self.temp, (self.width - 150, 50))
        draw_text("Press 'Esc' to exit", 13, self.temp, (self.width - 150, 70))

    def update(self):
        self.screen.blit(self.temp, self.temp.get_rect())
        pygame.display.update()
   
        
if __name__ == '__main__':
    file = 'worlds/world.yaml'
    if len(sys.argv) > 1:
        file = sys.argv[1]
    s = Screen(800, 600, 'GTSimulator', file)
    s.start()
