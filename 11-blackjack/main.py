import random
import os
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0  # blackjack

    if sum(card_list) >= 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)


def compare(usr_score, comp_score):
    if usr_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Lose, opponent has blackjack"
    elif usr_score == 0:
        return "Win with a Blackjack"
    elif usr_score > 21:
        return "Bust. You lose"
    elif comp_score > 21:
        return "Opponent bust. You win"
    elif usr_score > comp_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(logo)

    game_over = False
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score >= 21:
            game_over = True
        else:
            wants_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if wants_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, final score: {user_score}")
        print(f"Computer cards: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("clear")
    play_game()
