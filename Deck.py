'''
Shreeji Patel
Project 4 
Professor Smith
'''
import random
from Card import Card

class Deck:
    # Class attributes for card properties
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}  # Ace worth 1 point for simplicity

    def __init__(self):
        # Initialize the deck with all 52 cards
        self.cards = [Card(self.values[name], name, suit) for suit in self.suits for name in self.names]
        self.original_cards = self.cards.copy()  # Keep a copy of the original deck for resetting

    def shuffle(self):
        # Shuffle the deck randomly
        random.shuffle(self.cards)

    def draw(self, num=1):
        # Draw one or more cards from the deck
        if num > len(self.cards):
            raise ValueError("Cannot draw more cards than are in the deck")
        drawn_cards = [self.cards.pop() for _ in range(num)]
        return drawn_cards if num > 1 else drawn_cards[0]

    def place_card(self, card, position='top'):
        # Place a card back into the deck at a specified position
        if position == 'top':
            self.cards.insert(0, card)
        elif position == 'bottom':
            self.cards.append(card)
        else:
            self.cards.insert(position, card)

    def reset(self):
        # Reset the deck to its original state and shuffle
        self.cards = self.original_cards.copy()
        self.shuffle()

    def __len__(self):
        # Return the number of cards currently in the deck
        return len(self.cards)