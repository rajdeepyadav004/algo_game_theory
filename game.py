

class game:

	def __init__(self, num_rows, num_columns):
		self.num_rows = num_rows
		self.num_columns = num_columns		

	def set_utility_1(self, arg_utility):
		self.utility_1 = arg_utility

	def set_utility_2(self, arg_utility):
		self.utility_2 = arg_utility

	def best_response(self, player_num, move):
		'''best response of player 1'''
		'''player num can be 1 or 2'''
		'''move represents the move of the other player'''

		best_response_move = 0

		if(player_num == 1):
			current_max = self.utility_1[0][move]
			for i in range(self.num_columns):
				if (self.utility_1[i][move] > current_max):
					current_max = self.utility_1[i][move]
					best_response_move = i

		if(player_num == 2):
			current_max = self.utility_2[move][0]
			for i in range(self.num_rows):
				if (self.utility_2[move][i] > current_max):
					current_max = self.utility_2[move][i]
					best_response_move = i 


		'''returns the number of best response'''
		return best_response_move

	def max_min(self, player_num):
		pass

	def min_max(self, player_num):
		pass


	def print_game(self):
		for i in range(self.num_rows):
			print(" ".join([str(x) for x in zip(self.utility_1[i], self.utility_2[i])]))




if __name__ == '__main__':
	

	game1 = game(3,3)

	u1 = [[2,4,2],[1,2,4],[1,2,3]]
	u2 = [[3,4,2],[1,2,1],[2,7,3]]


	game1.set_utility_1(u1)
	game1.set_utility_2(u2)


	game1.print_game()
	print(game1.best_response(2, 2))

