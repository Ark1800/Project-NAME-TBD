import pygame
from screens.base_state import BaseState
from modules.push_button import Push_Button
from modules.grid import Grid
from modules.label import Label

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BROWN

class MainMenu(BaseState):
    def __init__(self):
        super().__init__()
        self.btn_start_game = Push_Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 100, "Start Game", 36)
        self.grid = Grid(50, BROWN)  
        

    def handle_events(self, events):
        for event in events:
            if self.btn_start_game.click(event):
                self.next_state = "GAMEPLAY"
                self.done = True

    def draw(self, screen):
        screen.fill((30, 30, 40)) 
        self.grid.draw(screen)  
        self.btn_start_game.draw(screen)
        