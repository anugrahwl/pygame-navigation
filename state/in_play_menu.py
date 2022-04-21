import pygame, sys
from pygame.locals import *
from state import State

class InPlayMenuState(State) :
    def __init__(self, states) :
        super().__init__(states)

        self.pointer_surf = pygame.Surface((10, 10))
        self.pointer_surf.fill('Red')

        self.pointer_rects = []
        self.pointer_index = 0

        self.options = ['resume', 'pokemon', 'bag', 'main menu']

        self.menu_surf = self.construct_menu()
        self.menu_rect = self.menu_surf.get_rect(center=(300, 250))

    def construct_menu(self) :
        margin = 20
        text_size = 30

        # generate text surfaces
        font_path = 'D:/Coding/Source Code/Pukimon/assets/font/04B_19.ttf'
        font = pygame.font.Font(font_path, text_size)

        text_surfaces = []
        for i, option in enumerate(self.options) :
            text_surf = font.render(option, True, 'Red')
            text_surfaces.append(text_surf)

        # calculate menu surface size
        main_width, main_height = 0, 0
        main_height = len(text_surfaces) * (text_size + margin) - margin

        for text_surf in text_surfaces :
            w, h = text_surf.get_size()
            if main_width < w :
                main_width = w
        main_width += 100

        # create menu surface and blit text surfaces into it
        menu_surf = pygame.Surface((main_width, main_height))
        menu_surf.fill('Black')
        for i, text_surf in enumerate(text_surfaces) :
            pos_x = main_width // 2
            pos_y = i * (margin + text_size)
            text_rect = text_surf.get_rect(midtop=(pos_x, pos_y))

            pos_x = text_rect.left - 15
            pos_y = text_rect.centery

            self.pointer_rects.append(self.pointer_surf.get_rect(center=(pos_x, pos_y)))

            menu_surf.blit(text_surf, text_rect)

        return menu_surf

    def execute_option(self) :
        match self.options[self.pointer_index] :
            case 'resume' :
                self.states.pop()
            case 'pokemon' :
                pass
            case 'bag' :
                pass
            case 'main menu' :
                self.states.pop()
                self.states.pop()

    def update(self, inputs) :
        if K_DOWN in inputs :
            self.pointer_index = (self.pointer_index + 1) % len(self.options)
        elif K_UP in inputs :
            self.pointer_index = (self.pointer_index - 1) % len(self.options)
        elif K_ESCAPE in inputs :
            self.states.pop()
        elif K_RETURN in inputs :
            self.execute_option()

    def render(self) :
        # render pointer on main surface
        menu_surf_copy = self.menu_surf.copy()
        menu_surf_copy.blit(self.pointer_surf, self.pointer_rects[self.pointer_index])

        # render main surface on screen
        self.screen.blit(menu_surf_copy, self.menu_rect)
