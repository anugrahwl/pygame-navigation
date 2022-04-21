import pygame
from state import State
from play_state import PlayState
from pygame.locals import *

class MainMenuState(State) :
    def __init__(self, states) :
        super().__init__(states)

        font_path = 'D:/Coding/Source Code/Pukimon/assets/font/04B_19.ttf'
        font = pygame.font.Font(font_path, 50)

        self.text_surf = font.render("Main Menu", True, "Red")
        self.text_rect = self.text_surf.get_rect(center=(300,100))

    def update(self, inputs) :
        if K_RETURN in inputs :
            play_state = PlayState(self.states)
            self.states.append(play_state)

    def render(self) :
        self.screen.fill('Black')
        self.screen.blit(self.text_surf, self.text_rect)
