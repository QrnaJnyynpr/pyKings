rules = """
 ______________________
| Ace   > Sniper\n
|       - Player can "snipe" any other player and force them to take a drink.
|       - Lasts until the next Sniper card is drawn.
 ______________________
| 2     > 2 Fingers
|       - Player must drink 2 fingers worth of their drink.
 ______________________
| 3     > 3 Fingers
|       - Player must drink 3 fingers worth of their drink.
 ______________________
| 4     > Toilet Card
|       - Entitles player to one free trip to the toilet during the game.
 ______________________
| 5     > Deprive
|       - Pick another player to "deprive" them of something during the game.
|       - Examples include using names, swearing, or making eye contact with
|		  other players.
|       - If they break the rule, they have to take a drink.
|       - Lasts until the next Deprive card is drawn.
 ______________________
| 6     > Categories
|       - Player picks a category, for example "car brands", or "Iron Maiden songs".
|       - Go around the table in a circle, and each player must name something
|		  from that category.
|       - First player to fail has to take a drink.
 ______________________
| 7     > Get to Heaven
|       - Player can stand up at any point, and the last person around the table to
|		  do the same must take a drink.
|       - Can be used multiple times. Lasts until the next Get to Heaven card is drawn.
 ______________________
| 8     > Pick a Mate
|       - Player picks a buddy who has to drink every single time the player has to.
|       - Lasts until the game is over.
 ______________________
| 9     > Hotline
|       - Player makes a phone ringing sound and puts their hand to their ear while
|		  making a phone gesture.
|       - Last person around the table to do the same has to take a drink.
|       - Can be used multiple times. Lasts until the next Hotline card is drawn.
 ______________________
| 10    > Make a Rule
|       - Player can add any new rule to be enforced, and include a forfeit for
|		  when a player fails to obey that rule.
|       - Lasts until the next Make a Rule card is drawn.
 ______________________
| Jack  > Thumb Card
|       - Player places their thumb on the edge of the table.
|       - The last person around the table to do the same has to take a drink.
|       - Can be used multiple times. Lasts until the next Thumb Card is drawn.
 ______________________
| Queen > Medusa
|       - When drawn, anyone around the table who makes direct eye contact with the
|		  player must take a drink.
|       - Lasts until the next Medusa card is drawn.
 ______________________
| King  > Dirty Pint
|       - Any time a King is drawn, the player must use their drink to fill the
|		  Kings pint glass up by one quarter.
|       - Whoever draws the fourth and final King, must drink the dirty pint.
"""

cards = [
	["Ace of Spades", "Sniper"],
	["Ace of Clubs", "Sniper"],
	["Ace of Hearts", "Sniper"],
	["Ace of Diamonds", "Sniper"],
	["2 of Spades", "Drink 2 fingers"],
	["2 of Clubs", "Drink 2 fingers"],
	["2 of Hearts", "Drink 2 fingers"],
	["2 of Diamonds", "Drink 2 fingers"],
	["3 of Spades", "Drink 3 fingers"],
	["3 of Clubs", "Drink 3 fingers"],
	["3 of Hearts", "Drink 3 fingers"],
	["3 of Diamonds", "Drink 3 fingers"],
	["4 of Spades", "Toilet Card"],
	["4 of Clubs", "Toilet Card"],
	["4 of Hearts", "Toilet Card"],
	["4 of Diamonds", "Toilet Card"],
	["5 of Spades", "Deprive"],
	["5 of Clubs", "Deprive"],
	["5 of Hearts", "Deprive"],
	["5 of Diamonds", "Deprive"],
	["6 of Spades", "Categories"],
	["6 of Clubs", "Categories"],
	["6 of Hearts", "Categories"],
	["6 of Diamonds", "Categories"],
	["7 of Spades", "Get to heaven"],
	["7 of Clubs", "Get to heaven"],
	["7 of Hearts", "Get to heaven"],
	["7 of Diamonds", "Get to heaven"],
	["8 of Spades", "Pick a mate"],
	["8 of Clubs", "Pick a mate"],
	["8 of Hearts", "Pick a mate"],
	["8 of Diamonds", "Pick a mate"],
	["9 of Spades", "Hotline"],
	["9 of Clubs", "Hotline"],
	["9 of Hearts", "Hotline"],
	["9 of Diamonds", "Hotline"],
	["10 of Spades", "Make a rule"],
	["10 of Clubs", "Make a rule"],
	["10 of Hearts", "Make a rule"],
	["10 of Diamonds", "Make a rule"],
	["Jack of Spades", "Thumb Card"],
	["Jack of Clubs", "Thumb Card"],
	["Jack of Hearts", "Thumb Card"],
	["Jack of Diamonds", "Thumb Card"],
	["Queen of Spades", "Medusa"],
	["Queen of Clubs", "Medusa"],
	["Queen of Hearts", "Medusa"],
	["Queen of Diamonds", "Medusa"],
	["King of Spades", "DIRTY PINT!!"],
	["King of Clubs", "DIRTY PINT!!"],
	["King of Hearts", "DIRTY PINT!!"],
	["King of Diamonds", "DIRTY PINT!!"],
]