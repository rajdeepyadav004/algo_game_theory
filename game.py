
import math
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
			current_max = -1*float('inf')
			for i in range(self.num_columns):
				if (self.utility_1[i][move] > current_max):
					current_max = self.utility_1[i][move]
					best_response_move = i

		if(player_num == 2):
			current_max = -1*float('inf')
			for i in range(self.num_rows):
				if (self.utility_2[move][i] > current_max):
					current_max = self.utility_2[move][i]
					best_response_move = i 


		'''returns the number of best response'''
		return best_response_move

	def max_min(self, player_num):
		'''returns the max_min strategy of the given player, given it works'''
		max_min_move = 0

		if(player_num == 1):
			current_max_min = -1*float('inf')
			for i in range(self.num_rows):
				current_min = float('inf')
				for j in range(self.num_columns):
					if(self.utility_1[i][j] < current_min):
						current_min = self.utility_1[i][j]
				if(current_min > current_max_min):
					current_max_min = current_min
					max_min_move = i

		if(player_num == 2):
			current_max_min = -1*float('inf')
			for j in range(self.num_columns):
				current_min = float('inf')
				for i in range(self.num_rows):
					if(self.utility_2[i][j] < current_min):
						current_min = self.utility_2[i][j]
				if(current_min > current_max_min):
					current_max_min = current_min
					max_min_move = j
		return max_min_move
	

	def min_max(self, player_num):
		'''returns the min_max strategy against the given player, given it works'''
		min_max_move = 0

		if(player_num == 1):
			current_min_max = float('inf')
			for j in range(self.num_columns):
				current_max = -1*float('inf')
				for i in range(self.num_rows):
					if(self.utility_1[i][j] > current_max):
						current_max = self.utility_1[i][j]
				if(current_max < current_min_max):
					current_min_max = current_max
					min_max_move = j

		if(player_num == 2):
			current_min_max = float('inf')
			for i in range(self.num_rows):
				current_max = -1*float('inf')
				for j in range(self.num_columns):
					if(self.utility_2[i][j] > current_max):
						current_max = self.utility_2[i][j]
				if(current_max < current_min_max):
					current_min_max = current_max
					min_max_move = i
		return min_max_move



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

