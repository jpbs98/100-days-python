with open("./Input/Names/invited_names.txt", mode="r", encoding="utf-8") as f:
    names = f.read().splitlines()
    names.remove("")


with open("./Input/Letters/starting_letter.txt", mode="r", encoding="utf-8") as f:
    letter = f.readlines()


for name in names:
    with open(
        f"./Output/ReadyToSend/letter_for_{name}.txt",
        mode="w",
        encoding="utf-8",
    ) as f:
        f.write(letter[0].replace("[name]", name))
        for line in letter[1:]:
            f.write(line)
