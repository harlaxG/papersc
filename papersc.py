import random

from secrets import choice

while True:
    print("Make your guess:", end=" ")
    guess = str(input())
    guess = guess.lower ()
    choices = ['rock', 'paper', 'scissors']
    computer_guess = random.choice(choices) 
    print('you guessed', guess)
    print('computer guessed', computer_guess)
    if guess in choices:
        if guess == computer_guess:
            print("tie")
        elif guess == 'rock':
             if computer_guess == 'scissors':
                 print('you win')
             elif computer_guess == 'paper':
                 print('you lose')   
        elif guess == 'paper':
            if computer_guess == 'scissors':
                print('you lose')
            elif computer_guess == 'rock':
                 print('you win')         
        elif guess == 'scissors':
            if computer_guess == 'rock':
                print('you dsdsdwlose')   
            elif computer_guess == 'paper':
                print('you win')
                   





# import random

# choice = ["rock","paper","scissors"]

# computer = random.choice(choices)
# player = None

# while player not in choices
# player = input("rock, paper, or scissors?: ")

# print("compuetr: ",computer)
# print("player: ",player)

# "rock" = 1
# "paper" = 2
# "scissors" = 3