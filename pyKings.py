import random
import pyfiglet
from configuration import rules, cards

kings_count = 0 # Store the number of King cups as they are drawn
player_list = []
draw_count = 0 # To show how many cards are left in the game

print(pyfiglet.figlet_format("-Welcome-\n--to-----\n-pyKings !-"))
print("                             Created by QrnaJnyynpr")
print("\n\n\nLet's play KINGS - The classic party drinking game\n\n\nPress ENTER to start the game,\nor type 'HELP' to learn how to play!\n")

intro = input().lower()

if intro == "help":
	print("\n")
	print(pyfiglet.figlet_format("How to Play:"))
	game_setup = "\n2+ players and a lot of alcohol needed!\n\n1. Place an empty pint glass in the middle of the table.\n2. Spread out a standard deck of cards in a circle around the glass.\n3. Each player must take it in turns to draw a card.\n4. For each card, the specific rule listed below must be enacted.\n5. Work around the table until all cards are drawn.\n\n"
	print(game_setup)
	print(pyfiglet.figlet_format("Cards:"))
	print(rules)
	print("Now let's get started!\n")

def choice():
	choice = random.choice(cards)
	if "King" in str(choice):
		global kings_count
		kings_count += 1
	line = "-" * len(choice[1])
	
	global draw_count
	
	if len(cards) > 0:
		if player_list != []:
			if draw_count == len(player_list):
				draw_count = 0
			player_turn = player_list[draw_count]

			print(f"\n\n\n >>>>> Player: {player_turn}")
		print(f"\n\n  __________________________________\n |								  \n | {choice[0]}\n | {line}\n | {choice[1]}\n | {line}\n | Cards left: {len(cards)-1} | Kings Count: {kings_count}/4\n |__________________________________\n\n")

		cards.remove(choice)
		draw_count += 1

def player_names():
	prompt = input("Would you like to add player names to\nkeep track of whose turn it is? y/n\n")
	if prompt == "yes" or prompt == "y":
		print("\nType a player name, then press ENTER to add each one.\nWhen you are finished, just type 'done' and press ENTER:\n")

		global player_list

		while True:
			name_entry = input()
			if name_entry.lower() != "done":
				player_list += [name_entry]
			else:
				print("\nLet's get started!\n\nYour first card is:")
				return
	print("\nStarting the game without player names!")

def letsplay():
	if len(cards) > 1:
		choice()
		next = input("\nPress ENTER to deal the next card:")
		while next != "":
			next = input("\nI said press ENTER. The ENTER KEY, you drunken mess!")
		letsplay()
	elif len(cards) == 1: 
		choice()
		print(pyfiglet.figlet_format("GAME OVER!"))
		input("Press ENTER to close!")

player_names()
letsplay()