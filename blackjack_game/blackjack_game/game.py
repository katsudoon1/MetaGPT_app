## game.py

import pygame
from deck import Deck
from player import Player
from database import Database

class Game:
    def __init__(self):
        self.player = Player()
        self.deck = Deck()
        self.bet_amount = 0
        self.balance = 0
        self.win_count = 0
        self.loss_count = 0

    def start_game(self):
        # Initialize game variables
        self.bet_amount = 0
        self.balance = Database().get_balance()
        self.win_count = Database().get_win_count()
        self.loss_count = Database().get_loss_count()

        # Deal initial cards
        self.deal_initial_cards()

        # Start game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        self.hit()
                    elif event.key == pygame.K_s:
                        self.stand()
                    elif event.key == pygame.K_d:
                        self.double_down()
                    elif event.key == pygame.K_p:
                        self.split()

            # Render game screen
            self.render_game_screen()

        pygame.quit()

    def place_bet(self, amount: int):
        self.bet_amount = amount

    def deal_initial_cards(self):
        for _ in range(2):
            card = self.deck.deal_card()
            self.player.deal_card(card)

    def hit(self):
        self.player.hit(self.deck)

    def stand(self):
        self.player.stand()

    def double_down(self):
        self.player.double_down(self.deck)

    def split(self):
        self.player.split(self.deck)

    def end_game(self):
        dealer_hand = self.player.get_current_hand()
        result = self.player.get_result(dealer_hand)

        # Update balance and win/loss count
        if result == "win":
            self.balance += self.bet_amount
            self.win_count += 1
        elif result == "loss":
            self.balance -= self.bet_amount
            self.loss_count += 1

        Database().update_balance(self.balance)
        Database().update_win_count(self.win_count)
        Database().update_loss_count(self.loss_count)

        # Render end game screen
        self.render_end_game_screen(result)

    def render_game_screen(self):
        # Render game screen logic here
        pass

    def render_end_game_screen(self, result: str):
        # Render end game screen logic here
        pass

    def update_balance(self, amount: int):
        self.balance += amount

    def update_win_loss_count(self, result: str):
        if result == "win":
            self.win_count += 1
        elif result == "loss":
            self.loss_count += 1
