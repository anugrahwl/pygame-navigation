import time, os, sys
import pygame
from library import extract_input
from pygame.locals import *
from state_stack import StateStack

class Game :
    def __init__(self) :
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

        self.running = True
        self.state_stack = StateStack()

    def get_events(self) :
        events = pygame.event.get()
        for event in events :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        return events

    def extract_input(events) :
        inputs = {}
        for event in events :
            if event.type == KEYDOWN :
                if event.key == K_RETURN :
                    inputs[K_RETURN] = True
                if event.key == K_UP :
                    inputs[K_UP] = True
                if event.key == K_DOWN :
                    inputs[K_DOWN] = True
                if event.key == K_ESCAPE :
                    inputs[K_ESCAPE] = True
        return inputs


    def loop(self) :
        while game.running:
            events = self.get_events()
            inputs = extract_input(events)

            self.state_stack.update(inputs)
            self.state_stack.render()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__" :
    game = Game()
    game.loop()
