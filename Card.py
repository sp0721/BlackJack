'''
Shreeji Patel
Project 4 
Professor Smith
'''

class Card:
    def __init__(self, value, name, suit):
        self.value = value  # Numeric value of the card (e.g., 10 for face cards)
        self.name = name    # Name of the card (e.g., "King", "7")
        self.suit = suit    # Suit of the card (e.g., "Hearts", "Spades")

    def __str__(self):
        # Returns a string representation of the card (e.g., "King of Hearts")
        return f"{self.name} of {self.suit}"

    def __repr__(self):
        # Returns the same string representation as __str__ for consistency
        return self.__str__()

    # Implementing the __add__ method to allow summing two cards or one card and an integer object
    def __add__(self, other):
        if isinstance(other, Card):
            # If adding two cards, sum their values
            return self.value + other.value
        elif isinstance(other, int):
            # If adding a card and an integer, add the integer to the card's value
            return self.value + other
        return NotImplemented  # Return NotImplemented for unsupported types

    # Implementing the __radd__ method to allow sum() to be used on an iterable of Cards
    def __radd__(self, other):
        # Calls __add__ method to handle the addition
        return self.__add__(other)