import sys
sys.path.append('D:/Coding/Source Code/pygame-navigation/state/')

from main_menu_state import MainMenuState

class StateStack :
    def __init__(self) :
        self.states = []
        self.states.append(MainMenuState(self.states))

    def update(self, inputs) :
        self.states[-1].update(inputs)

    def render(self) :
        for state in self.states :
            state.render()
