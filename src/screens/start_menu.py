import pygame
from src.screens.base_state import BaseState
from src.modules.push_button import Push_Button
from src.modules.grid import Grid
from src.modules.label import Label

from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BROWN

class MainMenu(BaseState):
    def __init__(self):
        super().__init__()
        self.btn_start_game = Push_Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100, 200, 100, "Setup", 36, "setup")
        self.btn_help = Push_Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 100, "Help", 36, "help")
        self.btn_exit = Push_Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 200, 200, 100, "Exit", 36, "exit")
        self.title = Label(SCREEN_WIDTH // 2, 100, 0, 100, "StablePlay", 100)

    def handle_events(self, events):
        for event in events:
            if self.btn_start_game.click(event):
                self.next_state = "GAMEPLAY"
                self.done = True
            elif self.btn_help.click(event):
                self.next_state = "HELP"
                self.done = True
            elif self.btn_exit.click(event):
                pygame.quit()
                sys.exit()

    def draw(self, screen):
        screen.fill((30, 30, 40)) 
        self.title.draw(screen)
        self.btn_start_game.draw(screen)
        self.btn_help.draw(screen)
        self.btn_exit.draw(screen)
        self.lbl_title.draw(screen)
    
        
