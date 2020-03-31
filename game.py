



class game:

	def __init__(self, num_rows, num_columns):
		self.num_rows = num_rows
		self.num_columns = num_columns		

	def set_utility_1(self, arg_utility):
		self.utility_1 = arg_utility

	def set_utility_2(self, arg_utility):
		self.utility_2 = arg_utility

	def arg_max_index(self,lst):
		t = 0
		current_max = lst[0]
		for i in range (len(lst)):
			if(current_max<lst[i]):
				current_max = lst[i]
				t = i

		return t

	def arg_max(self,lst):
		current_max = lst[0]
		for i in range (len(lst)):
			if(current_max<lst[i]):
				current_max = lst[i]

		return current_max

	def arg_min_index(self,lst):
		t = 0
		current_min = lst[0]
		for i in range (len(lst)):
			if(current_min>lst[i]):
				current_min = lst[i]
				t = i

		return t

	def arg_min(self,lst):
		current_min = lst[0]
		for i in range (len(lst)):
			if(current_min>lst[i]):
				current_min = lst[i]

		return current_min

	def get_row(self,player_num,row_num):

		return [self.utility_1[row_num][i] for i in range(self.num_columns)] if player_num == 1 else [self.utility_2[row_num][i] for i in range(self.num_columns)]

	def get_column(self,player_num,column_num):

		return [self.utility_1[i][column_num] for i in range(self.num_rows)] if player_num == 1 else [self.utility_2[i][column_num] for i in range(self.num_rows)]


	def best_response_move(self,player_num,move):
		return self.arg_max_index(self.get_column(1, move)) if player_num == 1 else self.arg_max_index(self.get_row(2,move))

	def best_response_utility(self,player_num,move):
		return self.arg_max(self.get_column(1, move)) if player_num == 1 else self.arg_max(self.get_row(2,move))

	def nash(self):
		nash_set = []
		for i in range(self.num_columns):
			move = self.best_response_move(1,i)
			if (self.best_response_move(2,move)==i):
				nash_element = (move,i)
				nash_set.append(nash_element)

		return nash_set

	def max_min_value(self,player_num):
		return self.arg_max([min(self.get_row(1,i)) for i in range(self.num_rows)]) if player_num == 1 else self.arg_max([min(self.get_column(2,i)) for i in range(self.num_columns)])

	def max_min_strategy(self,player_num):
		return self.arg_max_index([min(self.get_row(1,i)) for i in range(self.num_rows)]) if player_num == 1 else self.arg_max_index([min(self.get_column(2,i)) for i in range(self.num_columns)])
		

	def min_max_value(self,player_num):
		return self.arg_min([max(self.get_column(1,i)) for i in range(self.num_columns)]) if player_num == 1 else self.arg_min([max(self.get_row(2,i)) for i in range(self.num_rows)])

	def min_max_strategy(self,player_num):
		return self.arg_min_index([max(self.get_column(1,i)) for i in range(self.num_columns)]) if player_num == 1 else self.arg_min_index([max(self.get_row(2,i)) for i in range(self.num_rows)])
		
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
	print(game1.best_response_utility(1,2))
	print(game1.best_response_move(2,1))
	print(game1.max_min_strategy(1))
	print(game1.max_min_value(2))
	print(game1.min_max_strategy(1))
	print(game1.min_max_value(2))
	print(game1.nash())

