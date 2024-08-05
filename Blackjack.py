'''
Shreeji Patel
Project 4 
Professor Smith
'''


from Deck import Deck
from Hand import Hand

def main():
    # Requirement: Initialize a deck of cards
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    # Requirement: Deal initial cards
    player_hand.add_card(deck.draw())
    player_hand.add_card(deck.draw())
    dealer_hand.add_card(deck.draw())
    dealer_hand.add_card(deck.draw())

    # Requirement: Display initial hands
    print("Player's hand:", player_hand, "| Score:", player_hand.calculate_value())
    print("Dealer's hand: [Hidden, ", dealer_hand.cards[1], "]")

    # Requirement: Player's turn
    while True:
        player_value = player_hand.calculate_value()
        if player_value > 21:
            print("Player busts! Dealer wins.")
            break

        # Requirement: Allow player to hit or stand
        action = input("Do you want to hit (h) or stand (s)? ").lower()
        if action == 'h':
            player_hand.add_card(deck.draw())
            print("Player's hand:", player_hand, "| Score:", player_hand.calculate_value())
        elif action == 's':
            break
        else:
            print("Invalid action. Please choose 'h' or 's'.")

    # Requirement: Dealer's turn
    if player_value <= 21:
        print("Dealer's hand:", dealer_hand, "| Score:", dealer_hand.calculate_value())
        while dealer_hand.calculate_value() < 17:
            dealer_hand.add_card(deck.draw())
            print("Dealer's hand:", dealer_hand, "| Score:", dealer_hand.calculate_value())

        dealer_value = dealer_hand.calculate_value()
        player_value = player_hand.calculate_value()

        # Requirement: Determine the winner
        if dealer_value > 21:
            print("Dealer busts! Player wins.")
        elif player_value > dealer_value:
            print("Player wins!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    # Requirement: Display final hands and scores
    print("\nFinal Hands:")
    print("Player's hand:", player_hand, "| Score:", player_hand.calculate_value())
    print("Dealer's hand:", dealer_hand, "| Score:", dealer_hand.calculate_value())

if __name__ == "__main__":
    main()