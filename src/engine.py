import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK
from modules.push_button import Push_Button
from screens import MainMenu, Gameplay

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.virtual_screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.fullscreen = False
        self.clock = pygame.time.Clock()
        self.running = True

        self.state_dict = {
            "MAIN_MENU": MainMenu(),
            "GAMEPLAY": Gameplay()
        }
        
        self.active_state_name = "MAIN_MENU" #STARTING MENU
        self.state = self.state_dict[self.active_state_name]
        self.fullscreen_button = Push_Button(0, 0, 130, 36, "Fullscreen", 22)
        self.all_sprites = [] #USE FOR SPRITE GROUPS

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()
            if self.state.done:
                self.flip_state()
        pygame.quit()
        sys.exit()

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: #x button closes the window
                self.running = False
        self.state.handle_events(events)

    def update(self):
       # self.all_sprites.update() if sprites are decided to be used
        self.state.update()

    def draw(self):
        self.state.draw(self.screen)
        pygame.display.flip()
        
    def flip_state(self):
        next_state_name = self.state.next_state
        
        # Reset the old state's exit flags before leaving
        self.state.done = False
        self.state.next_state = None
        
        # Load the new active state (and optionally re-instantiate it to reset it)
        if next_state_name == "GAMEPLAY":
            self.state_dict["GAMEPLAY"] = Gameplay() # Clean slate reset
            
        self.active_state_name = next_state_name
        self.state = self.state_dict[self.active_state_name]
        
    