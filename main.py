'''
By: Andrew Campbell, Liam Johnston, Reese Hudson, and Gabriel Abdalla
Date: 2026-09-26
Program Details: a functional screen management application that measures the users stress levels and authenticates who they are in order to let them into certain applications.
'''
from src.engine import Game
import sys

if __name__ == "__main__":
    initial_state = "PRESAGE" if "--presage" in sys.argv else "MAIN_MENU"
    game = Game(initial_state)
    game.run()