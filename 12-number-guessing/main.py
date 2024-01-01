import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if mode == "easy":
    LIVES = 10
else:
    LIVES = 5

number = random.randint(1, 100)

while LIVES > 0:
    print(f"You have {LIVES} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess > number:
        print("Too high.")
        LIVES -= 1
    elif guess < number:
        print("Too low.")
        LIVES -= 1

    if LIVES == 0:
        print("You've run out of guesses, you lose.")
        break
    print("Guess again.")
