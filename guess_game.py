"""
rule:

computer will have a correct number. It will ask a player to put a number.
If the number matches, then the game is over and the player wins.
if the number does not match, computer will ask the player to put another number.

"""
import random


print("##########################################")
print("           Welcome to the game")
print("##########################################")

correct_number = random.randint(1, 10)
player_number = input("Put a number: ")
player_number = int(player_number)

while correct_number != player_number:
    print('Sorry, try again')
    player_number = input('retry: ')
    player_number = int(player_number)

print('Congratulation, you win the game')
