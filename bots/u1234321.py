https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder

import random

class Bot(object):

	def __init__(self):
		self.name = "1234321" # Put your id number her. String or integer will both work
		# Add your own variables here, if you want to. 

	def get_bid_game_type_collection(self, current_round, bots, game_type, winner_pays, artists_and_values, round_limit,
		starting_budget, painting_order, target_collection, my_bot_details, current_painting, winner_ids, amounts_paid):
		"""Strategy for collection type games. 

		Parameters:
		current_round(int): 			The current round of the auction game
		bots(dict): 					A dictionary holding the details of all of the bots in the auction
										Includes what paintings the other bots have won and their remaining budgets
		game_type(str): 				Will be "collection" for collection type games
		winner_pays(int):				Rank of bid that winner plays. 1 is 1st price auction. 2 is 2nd price auction.
		artists_and_values(dict):		A dictionary of the artist names and the painting value to the score (for value games)
		round_limit(int):				Total number of rounds in the game - will always be 200
		starting_budget(int):			How much budget each bot started with - will always be 1001
		painting_order(list str):		A list of the full painting order
		target_collection(list int):	A list of the type of collection required to win, for collection games - will always be [3,2,1]
										[5] means that you need 5 of any one type of painting
										[4,2] means you need 4 of one type of painting and 2 of another
										[3,2,1] means you need 3 of one type of painting, 2 of another, and 1 of another
		my_bot_details(dict):			Your bot details. Same as in the bots dict, but just your bot. 
										Includes your current paintings, current score and current budget
		current_painting(str):			The artist of the current painting that is being bid on
		winner_ids(list str):			A list of the ids of the winners of each round so far 
		amounts_paid(list int):			List of amounts paid for paintings in the rounds played so far 

		Returns:
		int:Your bid. Return your bid for this round. 
		"""

		# WRITE YOUR STRATEGY HERE FOR COLLECTION TYPE GAMES - FIRST TO COMPLETE A FULL COLLECTION

		my_budget = my_bot_details["budget"]
		return random.randint(0, my_budget)


	def get_bid_game_type_value(self, current_round, bots, game_type, winner_pays, artists_and_values, round_limit,
		starting_budget, painting_order, target_collection, my_bot_details, current_painting, winner_ids, amounts_paid):
		"""Strategy for value type games. 

		Parameters:
		current_round(int): 			The current round of the auction game
		bots(dict): 					A dictionary holding the details of all of the bots in the auction
										Includes what paintings the other bots have won and their remaining budgets
		game_type(str): 				Will be either "collection" or "value", the two types of games we will play
		winner_pays(int):				Rank of bid that winner plays. 1 is 1st price auction. 2 is 2nd price auction.
		artists_and_values(dict):		A dictionary of the artist names and the painting value to the score (for value games)
		round_limit(int):				Total number of rounds in the game
		starting_budget(int):			How much budget each bot started with
		painting_order(list str):		A list of the full painting order
		target_collection(list int):	A list of the type of collection required to win, for collection games
										[5] means that you need 5 of any one type of painting
										[4,2] means you need 4 of one type of painting and 2 of another
										[3,2,1] means you need 3 of one type of painting, 2 of another, and 1 of another
		my_bot_details(dict):			Your bot details. Same as in the bots dict, but just your bot. 
										Includes your current paintings, current score and current budget
		current_painting(str):			The artist of the current painting that is being bid on
		winner_ids(list str):			A list of the ids of the winners of each round so far 
		amounts_paid(list int):			List of amounts paid for paintings in the rounds played so far 

		Returns:
		int:Your bid. Return your bid for this round. 
		"""
		# WRITE YOUR STRATEGY HERE FOR VALUE GAMES - MOST VALUABLE PAINTINGS WON WINS

		# Here is an example of how to get the current painting's value
		current_painting_value = artists_and_values[current_painting]
		print("The current painting's value is ", current_painting_value)

		# Here is an example of printing who won the last round
		if current_round>1:
			who_won_last_round = winner_ids[current_round-1]
			print("The last round was won by ", who_won_last_round)

		# Play around with printing out other variables in the function, 
		# to see what kind of inputs you have to work with
		my_budget = my_bot_details["budget"]
		return random.randint(0, my_budget)

