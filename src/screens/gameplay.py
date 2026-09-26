import pygame
from src.screens.base_state import BaseState
from src.modules.listview import ListView
from src.settings import WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class Gameplay(BaseState):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont(None, 36)
        self.items = ["Program 1", "Program 2", "Program 3", "Program 4", "Program 5", "Program 6", "Program 7", "Program 8", "Program 9", "Program 10", "Program 11", "Program 12", "Program 13", "Program 14", "Program 15"]
        self.lst_blockedprograms = ListView(self.items, (SCREEN_WIDTH // 2) - 150, 100, 30)
        self.lst_blockedprograms.set_max_visible_items(5)
        self.lst_blockedprograms.set_width_override(300)  # Set the width of the ListView to 300 pixels

    def handle_events(self, events):
        self.lst_blockedprograms.handle_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Return to menu on Escape
                self.next_state = "MAIN_MENU"
                self.done = True

    def draw(self, screen):
        screen.fill((10, 50, 10))
        message = self.font.render("Gameplay - Press ESC to return to menu", True, WHITE)
        message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.lst_blockedprograms.draw(screen)
        screen.blit(message, message_rect)
        