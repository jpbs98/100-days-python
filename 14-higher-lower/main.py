import random
import os
from art import logo, vs
from game_data import data


def main():
    object_a = random.choice(data)
    object_b = random.choice(data)
    score = 0
    print(logo)

    while True:

        print(f"Compare A: {object_a['name']}, a {object_a['description']},"
              f" from {object_a['country']}.")
        print(vs)
        print(f"Compare B: {object_b['name']}, a {object_b['description']},"
              f" from {object_b['country']}.")

        guess = input("Who has more followers? Type 'A' or 'B': ")
        answer = higher_follower_count(object_a, object_b)

        if answer == 'A' and guess == "A":
            score += 1
            object_a = random.choice(data)

        if answer == 'B' and guess == "B":
            score += 1
            object_b = random.choice(data)

        if guess != answer:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"You're right! Current score: {score}.")


def higher_follower_count(obj1, obj2):
    if obj1["follower_count"] > obj2["follower_count"]:
        return "A"
    else:
        return "B"


if __name__ == '__main__':
    main()
