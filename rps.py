"""
Create a rock, paper, scissors game.

1. define a compare function between user and computer.
2. create computer options selected at random.
3. create game and replay option.
"""
from random import randint


# define a compare function between user and computer
def compare(user, computer):
    if user.lower() == computer:
        print("it is a tie.")
    elif user.lower() == 'rock':
        if computer == 'scissors':
            print('you win!')
        else:
            print('you lose. :(')
    elif user.lower() == 'paper':
        if computer == 'rock':
            print('you win!')
        else:
            print('you lose. :(')
    elif user.lower() == 'scissors':
        if computer == 'paper':
            print('you win!')
        else:
            print('you lose. :(')
    else:
        print('invalid option')
        return game_play()


# create computer options selected at random.
def computer_options():
    choices = ['rock', 'paper', 'scissors']
    choice_index = randint(0, 2)
    choice = choices[choice_index]
    return choice


# create game and replay option
def game_play():
    game = True

    while game:
        user = input('rock, paper, or scissors? ')
        computer = computer_options()
        compare(user, computer)

        play_again = input('would you like to play again? y/n: ')

        if play_again.lower() == 'y':
            return game_play()
        elif play_again.lower() == 'n':
            print('thanks for playing!')
            exit()
        else:
            print('invalid option.')
            return play_again


game_play()
