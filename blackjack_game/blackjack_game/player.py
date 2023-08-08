"""
player.py
Player class for managing the player's hand.
"""

class Player:
    def __init__(self):
        self.hands = [[]]
        self.current_hand_index = 0

    def get_current_hand(self) -> list:
        return self.hands[self.current_hand_index]

    def deal_card(self, card: str):
        self.hands[self.current_hand_index].append(card)

    def hit(self, deck: Deck):
        card = deck.deal_card()
        self.hands[self.current_hand_index].append(card)

    def stand(self):
        self.current_hand_index += 1
        self.hands.append([])

    def double_down(self, deck: Deck):
        self.hit(deck)
        self.stand()

    def split(self, deck: Deck):
        card = self.hands[self.current_hand_index].pop()
        self.hands.append([card])
        self.hit(deck)

    def get_hand_value(self, hand: list) -> int:
        value = 0
        num_aces = 0
        for card in hand:
            if card in ["J", "Q", "K"]:
                value += 10
            elif card == "A":
                value += 11
                num_aces += 1
            else:
                value += int(card)

        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value

    def is_blackjack(self, hand: list) -> bool:
        return len(hand) == 2 and self.get_hand_value(hand) == 21

    def is_bust(self, hand: list) -> bool:
        return self.get_hand_value(hand) > 21

    def get_result(self, dealer_hand: list) -> str:
        player_hand = self.get_current_hand()

        if self.is_bust(player_hand):
            return "loss"
        elif self.is_bust(dealer_hand):
            return "win"
        elif self.is_blackjack(player_hand) and not self.is_blackjack(dealer_hand):
            return "win"
        elif not self.is_blackjack(player_hand) and self.is_blackjack(dealer_hand):
            return "loss"
        elif self.get_hand_value(player_hand) > self.get_hand_value(dealer_hand):
            return "win"
        elif self.get_hand_value(player_hand) < self.get_hand_value(dealer_hand):
            return "loss"
        else:
            return "push"
