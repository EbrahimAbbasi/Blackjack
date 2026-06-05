import random
# Created by Ebrahim Abbasi @ Exopi ea@Exopi.dk
# Create deck
card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(ebi, category) for category in card_categories for ebi in card_list]

# Shuffle deck
random.shuffle(deck)


def card_value(card):
    """Return the base value of a card."""
    rank = card[0]

    if rank in ['Jack', 'Queen', 'King']:
        return 10
    elif rank == 'Ace':
        return 11
    else:
        return int(rank)


def calculate_score(cards):
    """Calculate score with Ace adjustment."""
    score = sum(card_value(card) for card in cards)
    # Count number of Aces
    aces = sum(1 for card in cards if card[0] == 'Ace')

    # Convert Aces from 11 to 1 if needed
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score


# Initial deal (Card pick up)
player_cards = [deck.pop(), deck.pop()]
dealer_cards = [deck.pop(), deck.pop()]

# =====================
# PLAYER TURN
# =====================

while True:
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print("\n--------------------")
    print("Your Cards:", player_cards)
    print("Your Score:", player_score)

    print("Dealer's Visible Card:", dealer_cards[0])
    print("--------------------")

    # Check for player bust
    if player_score > 21:
        print("\nDealer wins! You busted.")
        break

    choice = input(
        'What do you want? ["hit" to draw another card, "stand" to stand]: '
    ).lower()

    if choice == "hit":
        new_card = deck.pop()
        player_cards.append(new_card)
        print(f"\nYou drew: {new_card}")

    elif choice == "stand":
        break

    else:
        print("Invalid choice. Please try again.")



# =====================
# DEALER TURN
# =====================

if player_score <= 21:

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    # =====================
    # NATURAL BLACKJACK CHECK
    # =====================

    player_natural_blackjack = (
        player_score == 21 and len(player_cards) == 2
    )

    dealer_natural_blackjack = (
        dealer_score == 21 and len(dealer_cards) == 2
    )

    # Both have Natural Blackjack
    if player_natural_blackjack and dealer_natural_blackjack:

        print("\n====================")
        print("Dealer reveals hand:")
        print("Dealer Cards:", dealer_cards)
        print("Dealer Score:", dealer_score)

        print("\nYour Cards:", player_cards)
        print("Your Score:", player_score)
        print("====================")

        print("\nBoth have Natural Blackjack! It's a tie!")

    # Player only has Natural Blackjack
    elif player_natural_blackjack:

        print("\n====================")
        print("Dealer reveals hand:")
        print("Dealer Cards:", dealer_cards)
        print("Dealer Score:", dealer_score)

        print("\nYour Cards:", player_cards)
        print("Your Score:", player_score)
        print("====================")

        print("\nNatural Blackjack! Player wins!")

    # Dealer only has Natural Blackjack
    elif dealer_natural_blackjack:

        print("\n====================")
        print("Dealer reveals hand:")
        print("Dealer Cards:", dealer_cards)
        print("Dealer Score:", dealer_score)

        print("\nYour Cards:", player_cards)
        print("Your Score:", player_score)
        print("====================")

        print("\nDealer has Natural Blackjack! Dealer wins!")

    else:

        # Dealer draws until 17 or more
        while calculate_score(dealer_cards) < 17:
            new_card = deck.pop()
            dealer_cards.append(new_card)

        dealer_score = calculate_score(dealer_cards)
        player_score = calculate_score(player_cards)

        print("\n====================")
        print("Dealer reveals hand:")
        print("Dealer Cards:", dealer_cards)
        print("Dealer Score:", dealer_score)

        print("\nYour Cards:", player_cards)
        print("Your Score:", player_score)
        print("====================")

        # Determine winner
        if dealer_score > 21:
            print("\nPlayer wins! Dealer busted.")

        elif player_score > dealer_score:
            print("\nPlayer wins! Higher score.")

        elif dealer_score > player_score:
            print("\nDealer wins! Higher score.")

        else:
            print("\nIt's a tie!")

# Final results
print("\n===== FINAL RESULT =====")
print("Player Cards:", player_cards)
print("Player Score:", calculate_score(player_cards))
print("\nDealer Cards:", dealer_cards)
print("Dealer Score:", calculate_score(dealer_cards))