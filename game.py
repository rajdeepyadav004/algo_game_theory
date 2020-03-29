

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

	def nash(self):
		nash_set = []
		for i in range(self.num_columns):
			move = self.best_response(1,i)
			if (self.best_response(2,move)==i):
				nash_element = (move,i)
				nash_set.append(nash_element)

		return nash_set

	def max_min(self, player_num):
		if player_num==1:
			return max([min(x) for x in self.utility_1])
		else:	
			min_of_columns = [0]*self.num_columns
			for i in range(self.num_columns):
				min_of_columns[i] = min([x[i] for x in self.utility_2])
			return max(min_of_columns)

	def min_max(self, player_num):
		if player_num == 1:
			max_of_rows = [0]*self.num_rows
			for i in range(self.num_rows):
				max_of_rows[i] = max([x[i] for x in self.utility_1])
			return min(max_of_rows)
		else:
			return min([max(x) for x in self.utility_2])
		

	def print_game(self):
		for i in range(self.num_rows):
			print(" ".join([str(x) for x in zip(self.utility_1[i], self.utility_2[i])]))




if __name__ == '__main__':
	

	game1 = game(3,3)

	u1 = [[6,8,0],[10,5,2],[8,20,4]]
	u2 = [[6,20,8],[0,5,8],[0,0,4]]


	game1.set_utility_1(u1)
	game1.set_utility_2(u2)


	game1.print_game()
	print(game1.best_response(2, 2))
	print(game1.max_min(1))
	print(game1.max_min(2))
	print(game1.min_max(1))
	print(game1.min_max(2))
	print(game1.nash())

