import pygame

class State :
    def __init__(self, states) :
        self.screen = pygame.display.get_surface()
        self.states = states
