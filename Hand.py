'''
Shreeji Patel
Project 4 
Professor Smith
'''

class Hand:
    def __init__(self):
        self.cards = []  # Initialize an empty list to hold the cards in the hand

    def add_card(self, card):
        # Add a card to the hand
        self.cards.append(card)

    def discard_card(self, card):
        # Remove a specific card from the hand
        self.cards.remove(card)

    def calculate_value(self):
        # Calculate the total value of the hand
        value = sum(self.cards)  # Sum the values of all cards in the hand
        # Adjust for Aces (if you want to implement the official 1/11 rule, you can modify here)
        num_aces = sum(1 for card in self.cards if card.name == 'Ace')  # Count the number of Aces
        while value > 21 and num_aces:
            value -= 10  # Adjust the value by subtracting 10 for each Ace if the total value is over 21
            num_aces -= 1
        return value

    def __len__(self):
        # Return the number of cards in the hand
        return len(self.cards)

    def __str__(self):
        # Return a string representation of the hand, listing all cards
        return ', '.join(str(card) for card in self.cards)