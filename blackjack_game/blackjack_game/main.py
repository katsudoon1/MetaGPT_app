"""
main.py
Main entry point of the blackjack game.
"""

import pygame
from game import Game

def main():
    pygame.init()

    game = Game()
    game.start_game()

    pygame.quit()

if __name__ == "__main__":
    main()
