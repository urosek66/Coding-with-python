import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
choices = [rock, paper, scissors]

if user_choice > 2 or user_choice < 0:
    print("Your number is invalid you lose the game!")
else:
    print(choices[user_choice])
    print("Computer chose:")
    print(choices[computer_choice])

    if user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You won!")
    elif user_choice == 0 and computer_choice == 2:
        print("You won!")
    elif user_choice < computer_choice:
        print("You lose!")
    elif user_choice == computer_choice:
        print("It's a draw!")
