print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

calc = total / people * (1 + (percent / 100))

print(f"Each person should pay: ${round(calc, 2)}")
