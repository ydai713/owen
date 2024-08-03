"""
rule:

computer will have a correct number. It will ask a player to put a number.
If the number matches, then the game is over and the player wins.
if the number does not match, computer will ask the player to put another number.


TODO:
the user only has 3 chances to guess the correct number.
if the user does not guess the correct number in 3 chances, then the game is over.
"""
import random


def main():

    # print the game title
    print_game_title()
    
    # generate a random correct number
    correct_number = generate_random_number()
    
    # ask player to put a number
    player_number = receive_user_input()
    
    while correct_number != player_number:
        print('Sorry, try again')
        player_number = receive_user_input()
    
    print('Congratulation, you win the game')


def receive_user_input():
    player_number = input("Put a number: ")
    player_number = int(player_number)
    return 

def generate_random_number():
    return random.randint(1, 10)

def print_game_title():
    print("##########################################")
    print("           Welcome to the game")
    print("##########################################")


if __name__ == "__main__":
    main()
