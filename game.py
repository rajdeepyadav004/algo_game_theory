

def arg_max(lst):
	max_value = max(lst[i] for i in range(len(lst)))
	arg_max_set = []
	for i in range (len(lst)):
		if(lst[i] == max_value):
			arg_max_set.append(i)

	return arg_max_set


def arg_min(lst):
	min_value = min(lst[i] for i in range(len(lst)))
	arg_min_set = []
	for i in range (len(lst)):
		if(lst[i] == min_value):
			arg_min_set.append(i)

	return arg_min_set



class game:

	def __init__(self, num_rows, num_columns):
		self.num_rows = num_rows
		self.num_columns = num_columns		

	def set_utility_1(self, arg_utility):
		self.utility_1 = arg_utility

	def set_utility_2(self, arg_utility):
		self.utility_2 = arg_utility


	def get_row(self,player_num,row_num):

		return [self.utility_1[row_num][i] for i in range(self.num_columns)] if player_num == 1 else [self.utility_2[row_num][i] for i in range(self.num_columns)]

	def get_column(self,player_num,column_num):

		return [self.utility_1[i][column_num] for i in range(self.num_rows)] if player_num == 1 else [self.utility_2[i][column_num] for i in range(self.num_rows)]

	
	def best_response_move(self,player_num,move):
		return arg_max(self.get_column(1, move)) if player_num == 1 else arg_max(self.get_row(2,move))

	def best_response_utility(self,player_num,move):
		t = self.best_response_move(player_num, move)[0]
		return self.utility_1[t][move] if player_num == 1 else self.utility_2[move][t]

	def nash(self):
		nash_set = []
		for i in range(self.num_columns):
			move_set = self.best_response_move(1,i)
			nash_element_set = list(map(lambda move: (move,i), list(filter(lambda x: i in self.best_response_move(2,x) , move_set))))
			nash_set.extend(nash_element_set)

		return nash_set

	def max_min_value(self,player_num):
		t = self.max_min_strategy(player_num)[0]
		return min(self.get_row(1,t)) if player_num == 1 else min(self.get_column(2,t))

	def max_min_strategy(self,player_num):
		return arg_max([min(self.get_row(1,i)) for i in range(self.num_rows)]) if player_num == 1 else arg_max([min(self.get_column(2,i)) for i in range(self.num_columns)])
		

	def min_max_value(self,player_num):
		'''gives the utility of player_num when the other player plays the min-max strategy against him'''
		t = self.min_max_strategy(player_num)[0]
		return max(self.get_column(1,t)) if player_num == 1 else max(self.get_row(2,t))

	def min_max_strategy(self,player_num):
		'''gives the min-max strategy against player_num'''
		return arg_min([max(self.get_column(1,i)) for i in range(self.num_columns)]) if player_num == 1 else arg_min([max(self.get_row(2,i)) for i in range(self.num_rows)])
		
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

