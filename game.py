
import copy

def get_reduced_matrix(matrix, rows, columns):
	return [[matrix[row][col] for col in columns] for row in rows]


def get_row(matrix, num_row):
	return matrix[num_row]

def get_column(matrix, num_col):
	return [row[num_col] for row in matrix] 

def arg_min(lst):
	min_value = min(lst)
	equal_to_min = lambda x: x[1] == min_value 
	return [x[0] for x in filter(equal_to_min, enumerate(lst))] 


def arg_max(lst):
	max_value = max(lst)
	equal_to_max = lambda x: x[1] == max_value
	return [x[0] for x in filter(equal_to_max, enumerate(lst))]


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
		return arg_max(get_column(self.utility_1, move)) if player_num == 1 else arg_max(get_row(self.utility_2, move))


	def max_min(self, player_num):
		if player_num==1:
			return arg_max([min(get_row(self.utility_1, i)) for i in range(self.num_rows)])
		else:	
			return arg_max([min(get_column(self.utility_2, i)) for i in range(self.num_columns)])

	def min_max(self, player_num):
		if player_num==1:
			return arg_min([max(get_column(self.utility_1, i)) for i in range(self.num_rows)])
		else:	
			return arg_min([max(get_row(self.utility_2, i)) for i in range(self.num_columns)])
		

	def nash_brute_force(self):
		nash_set = []
		for row in range(self.num_rows):
			for column in range(self.num_columns):
				if(row in arg_max(get_column(self.utility_1, column)) and column in arg_max(get_row(self.utility_2, row))):
					nash_set.append((row,column))

		return nash_set 



	def nash_helper(self, rows, columns):

		reduced_utility_1 = get_reduced_matrix(self.utility_1, rows, columns)
		reduced_utility_2 = get_reduced_matrix(self.utility_2, rows, columns)

		nash_set = []
		for column in columns:
			best_response_1 = arg_max(get_column( reduced_utility_1, column))
			for row in best_response_1:
				if (column in arg_max(get_row(reduced_utility_2, row))):
					nash_set.append((row, column))
		return nash_set


	def nash_method_2(self):
		return self.nash_helper(range(self.num_rows), range(self.num_columns))

	def nash_elimination(self):
		
		row_list = range(self.num_rows)
		column_list = range(self.num_columns)

		updated = True


		while(updated):
			updated = False
			temp_row_list = copy.deepcopy(row_list)
			temp_column_list = copy.deepcopy(column_list)

			for row1 in row_list:
				for row2 in row_list:

					first_dominated, second_dominated = True, True

					for col in column_list:

						if(self.utility_1[row1][col] >= self.utility_1[row2][col]):
							first_dominated = False

						if(self.utility_1[row1][col] <= self.utility_1[row2][col]):
							second_dominated = False

					if(first_dominated):
						temp_row_list.remove(row1)

					if(second_dominated):
						temp_row_list.remove(row2)


			row_list = temp_row_list


			for col1 in column_list:
				for col2 in column_list:

					first_dominated, second_dominated = True, True

					for row in row_list:
						if(self.utility_2[row][col1] >= self.utility_2[row][col2]):
							first_dominated = False

						if(self.utility_2[row][col1] <= self.utility_2[row][col2]):
							second_dominated = False

					if(first_dominated):
						updated = True
						temp_column_list.remove(col1)

					if(second_dominated):
						updated = False
						temp_column_list.remove(col2)

			column_list = temp_column_list

		return self.nash_helper(row_list, column_list)



	def print_game(self):
		for i in range(self.num_rows):
			print(" ".join([str(x) for x in zip(self.utility_1[i], self.utility_2[i])]))




if __name__ == '__main__':
	

	game1 = game(3,3)

	u1 = [[4,0,2],[0,1,0],[0,0,1]]
	u2 = [[4,2,2],[0,1,2],[0,2,1]]


	game1.set_utility_1(u1)
	game1.set_utility_2(u2)


	game1.print_game()
	
	print(game1.min_max(1))
	print(game1.min_max(2))
	print(game1.max_min(1))
	print(game1.max_min(2))
	print(game1.nash_brute_force())
	print(game1.nash_method_2())
	print(game1.nash_elimination())



