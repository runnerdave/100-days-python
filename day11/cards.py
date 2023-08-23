import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def rank(self):
        return self.rank
    
    def suit(self):
        return self.suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

# Example usage:
# deck = Deck()
# print(deck)  # Output: Deck of 52 cards

# deck.shuffle()
# print(deck.cards)  # Output: Shuffled deck of cards

# card = deck.draw_card()
# print(card)  # Output: A randomly drawn card