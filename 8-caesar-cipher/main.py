import art


def caesar(message, shift_int, action):
    cipher_msg = ""

    for char in message:
        if char not in alphabet:
            cipher_msg += char
            continue
        idx = alphabet.index(char)
        if action == "encode":
            cipher_msg += alphabet[(idx + shift_int % len(alphabet)) % len(alphabet)]
        else:
            cipher_msg += alphabet[(idx - shift_int % len(alphabet)) % len(alphabet)]

    print(f"Here's the {action}d result: {cipher_msg}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    keep_going = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if keep_going != "yes":
        print("Goodbye")
        break
