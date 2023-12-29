import os
from art import logo

print(logo)

auction = {}
bidders = True

while bidders:
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    auction[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders != "yes":
        bidders = False
    os.system("clear")

winner_name, winner_bid = "", 0

for name, bid in auction.items():
    if bid > winner_bid:
        winner_name = name
        winner_bid = bid

print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
