from functools import reduce

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


	def reduced_game_nash(self):
		get_row_set = [self.get_row(1,i) for i in range(self.num_rows)]
		get_column_set = [self.get_column(2,i) for i in range(self.num_columns)]

		for p in range(max(self.num_rows,self.num_columns)):
			for i in range(len(get_row_set)):
				current_row = get_row_set[i]
				v = list(filter(lambda y: reduce(lambda r,s: r and s,[current_row[j] < y[j] for j in range(len(get_row_set[0]))] ), list(filter(lambda x: x != current_row, get_row_set)) ))
				if len(v) != 0:
					del get_row_set[i]
					for k in range(len(get_column_set)):
						del(get_column_set[k])[i]

			for t in range(len(get_column_set)):
				current_column = get_column_set[t]
				v = list(filter(lambda y: reduce(lambda r,s: r and s, [current_column[j] < y[j] for j in range(len(get_column_set[0]))]), list(filter(lambda x: x!= current_column, get_column_set)) ))
				if len(v) != 0:
					del get_column_set[t]
					for k in range(len(get_row_set)):
						del(get_row_set[k])[t]
			
		column_set = []
		for j in range(len(get_column_set[0])):
			column_set_element = [get_column_set[i][j] for i in range(len(get_column_set))]
			column_set.append(column_set_element)

		return (get_row_set, column_set)

	
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

	u1 = [[10,5,3],[0,4,6],[2,3,2]]
	u2 = [[4,3,2],[1,6,0],[1,5,8]]


	game1.set_utility_1(u1)
	game1.set_utility_2(u2)

	(z1, z2) = game1.reduced_game_nash()
	reduced_game = game((len(z1)), (len(z2)) )
	reduced_game.set_utility_1(z1)
	reduced_game.set_utility_2(z2)


	game1.print_game()
	print(game1.best_response_utility(1,2))
	print(game1.best_response_move(2,1))
	print(game1.max_min_strategy(1))
	print(game1.max_min_value(2))
	print(game1.min_max_strategy(1))
	print(game1.min_max_value(2))
	print(game1.nash())
	print(reduced_game.nash())

