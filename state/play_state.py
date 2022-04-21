import pygame
from pygame.locals import *
from state import State
from in_play_menu import InPlayMenuState

class PlayState(State) :
    def __init__(self, states) :
        super().__init__(states)

        font_path = 'D:/Coding/Source Code/Pukimon/assets/font/04B_19.ttf'
        font = pygame.font.Font(font_path, 50)

        self.text_surf = font.render("Play", True, "Red")
        self.text_rect = self.text_surf.get_rect(center=(300,100))

    def update(self, inputs) :
        if K_RETURN in inputs :
            self.states.append(InPlayMenuState(self.states))

    def render(self) :
        self.screen.fill('Black')
        self.screen.blit(self.text_surf, self.text_rect)
