import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

# user choice
choice = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ).lower()
)
if choice > 2 or choice < 0:
    print("You typed an invalid number.")
    quit()

print(choices[choice])

# computer choice
comp_choice = random.randint(0, 2)
print("Computer chose:\n", choices[comp_choice])

# 0 is rock, 1 is paper and 2 is scissors
if choice == 0 and comp_choice == 2:
    print("You win!")
elif choice == 0 and comp_choice == 1:
    print("You lose!")
elif choice == 1 and comp_choice == 2:
    print("You lose!")
elif choice == 1 and comp_choice == 0:
    print("You win!")
elif choice == 2 and comp_choice == 0:
    print("You lose!")
elif choice == 2 and comp_choice == 1:
    print("You win!")
else:
    print("Draw")
