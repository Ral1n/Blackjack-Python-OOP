import random

suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Ace', 'Jack', 'Queen', 'King']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine': 9, 'Ten':10, 'Ace':11, 'Jack':10, 'Queen':10, 'King':10}

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return f'{self.rank} of {self.suit}'

class Deck:

	def __init__(self):

		self.all_cards = []

		for rank in ranks:
			for suit in suits:
				card = Card(suit, rank)
				self.all_cards.append(card)

	def shuffle(self):

		random.shuffle(self.all_cards)
		print('The deck has been shuffled')

	def deal_one(self):

		return self.all_cards.pop()


class Player:

	def __init__(self, balance):

		self.balance = balance

def ask_bet(balance):

	bet = 'WRONG'

	while bet.isdigit() == False or int(bet) > balance:

		bet = input('How much money do you want to bet?')

		if bet.isdigit() == False:
			print('This amount is not valid')
		elif int(bet) > balance:
			print('This amount is above your balance')

	return int(bet)

def ask_choice():

	choice = 'WRONG'

	accepted_values = ['S', 'H']

	while choice not in accepted_values:

		choice = input('HIT (H) or STAY (S) : ')

		if choice not in accepted_values:
			print('Invalid choice')

	return choice


def gameon_choice():

	choice = 'WRONG'

	accepted_values = ['Y', 'N']

	while choice not in accepted_values:

		choice = input('Do you want to play another round? (Y or N): ')

		if choice not in accepted_values:
			print('I dont understand!')

	if choice == "Y":
		return True
	else:
		return False


# GAME LOGIC 

deck = Deck()

player = Player(500)

game_on = True

# while game_on:

# 	deck.shuffle()
# 	print(f'Your balance: {player.balance}')

# 	bet = ask_bet(player.balance)

# 	dealer_cards = []
# 	player_cards = []

# 	for i in range(2):
# 		player_cards.append(deck.deal_one())
# 		dealer_cards.append(deck.deal_one())

# 	player_score = player_cards[0].value + player_cards[1].value
# 	dealer_score = dealer_cards[0].value + dealer_cards[1].value 
	
# 	cards_dealt_to_player = 2
# 	cards_dealt_to_dealer = 2

# 	print(f'Your cards: {player_cards[0]}, {player_cards[1]} ({player_score})')
# 	print(f'Dealer cards: {dealer_cards[0]}, HIDDEN')

# 	choice = ask_choice()

# 	while choice == 'H':

# 		player_cards.append(deck.deal_one())
		
# 		player_score = player_score + player_cards[cards_dealt_to_player].value
		
# 		if player_score <= 21:
# 			print(f'You got {player_cards[cards_dealt_to_player]} => {player_score}')
# 			choice = ask_choice()
# 		else:
# 			print(f'You got {player_cards[cards_dealt_to_player]} => BUST! ({player_score})')
# 			break

# 		cards_dealt_to_player += 1

# 	print(f'Dealer cards: {dealer_cards[0]}, {dealer_cards[1]} ({dealer_score})')

# 	while dealer_score <= 17:

# 		dealer_cards.append(deck.deal_one())
		
# 		dealer_score = dealer_score + dealer_cards[cards_dealt_to_dealer].value
		
# 		print(f'Dealer got {dealer_cards[cards_dealt_to_dealer]} => {dealer_score}')
		
# 		cards_dealt_to_dealer += 1

# 	if player_score < dealer_score or (player_score == 21 and dealer_score != 21):
# 		player.balance += 2*bet
# 		print(f'You won ${2*bet}! Balance: {player.balance}')
# 	elif player_score == 21 and dealer_score == 21:
# 		player.balance += bet
# 		print(f'Tie! You got your bet back. Balance: {player.balance}')
# 	elif dealer_score < player_score or (dealer_score == 21 and player_score != 21): 
# 		player.balance -= bet
# 		print(f'Dealer won! You lost ${bet}! Balance: {player.balance}')

# 	game_on = gameon_choice()
