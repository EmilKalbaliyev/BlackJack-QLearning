import random


class Hand:

    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
    suits = ['H', 'S', 'D', 'C']

    def __init__(self):
        self.hand = []
        self.total = 0
        self.aces = 0
        self.first = 0
        self.terminated = False
        self.bust = False
        self.doubleDown = False
        return

    def sum(self, card):
        if card < 8:
            self.total += int(card) + 2
        elif card == 12:
            self.total += 11
        else:
            self.total += 10
        while self.total > 21 and self.aces > 0:
            self.total -= 10
            self.aces -= 1
        if self.total > 21:
            self.bust = True
            self.terminated = True

    def add(self, number_of_cards, suit=None, card=None):
        for i in range(0, number_of_cards):
            if suit is None or card is None:
                suit = random.randint(0, len(self.suits) - 1)
                card = random.randint(0, len(self.cards) - 1)
            if self.cards[card] == 'A':
                self.aces += 1
            self.hand.append((self.suits[suit] + self.cards[card]))
            self.sum(card)
            suit = card = None
            if len(self.hand) == 1:
                self.first = self.get_total()

    def terminate(self):
        self.terminated = True

    def set_double_down(self):
        self.doubleDown = True

    def get_total(self):
        return self.total

    def is_bust(self):
        return self.bust

    def is_twenty_one(self):
        return self.total == 21

    def is_terminated(self):
        return self.terminated

    def is_double_down(self):
        return self.doubleDown


