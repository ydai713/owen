"""
rule:

computer will have a correct number. It will ask a player to put a number.
If the number matches, then the game is over and the player wins.
if the number does not match, computer will ask the player to put another number.

hint: use while loop
"""

print("##########################################")
print("           Welcome to the game")
print("##########################################")

correct_number = 5
player_number = input("Put a number: ")
player_number = int(player_number)

if correct_number == player_number:
    print("hooray, you win!")
