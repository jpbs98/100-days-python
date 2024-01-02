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
        print(
            f"Compare A: {object_a['name']}, a {object_a['description']},"
            f" from {object_a['country']}."
        )
        print(vs)
        print(
            f"Against B: {object_b['name']}, a {object_b['description']},"
            f" from {object_b['country']}."
        )

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        answer = higher_follower_count(object_a, object_b)

        if guess != answer[0]:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

        if (answer[0] == "A" and guess == "A") or (answer[0] == "B" and guess == "B"):
            score += 1
            object_a = answer[1]
            object_b = random.choice(data)

        os.system("cls" if os.name == "nt" else "clear")
        print(logo)
        print(f"You're right! Current score: {score}.")


def higher_follower_count(obj_a, obj_b):
    # return opposing object for swap to object_a
    if obj_a["follower_count"] > obj_b["follower_count"]:
        return "A", obj_b
    else:
        return "B", obj_a


if __name__ == "__main__":
    main()
