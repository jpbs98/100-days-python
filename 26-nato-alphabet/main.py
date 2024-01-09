import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

code = {row.letter: row.code for _, row in df.iterrows()}

input_word = input("Enter a word: ").upper()

output_list = [code[letter] if letter in code else letter for letter in input_word]
print(output_list)
