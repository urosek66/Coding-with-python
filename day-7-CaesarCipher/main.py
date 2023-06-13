from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# define function caesar()


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:

        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f"Here's the {cipher_direction}d result: {end_text}")


# import and show logo
print(logo)

# define while loop to play game
play_again = True
while play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    new_game = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if new_game == "yes":
        play_again = True
    elif new_game == "no":
        play_again = False
        print("Goodbye")
    else:
        play_again = False
        print("You should write 'yes' or 'no'.")


    