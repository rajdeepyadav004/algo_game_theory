

def get_row(matrix, num_row):
	return matrix[num_row]

def get_column(matrix, num_col):
	return [row[num_col] for row in matrix] 

def arg_min(lst):

	### VIRGIN METHOD ###
	res = 0
	curr_min = lst[0]
	for i in range(len(lst)):
		if lst[i] < curr_min:
			curr_min = lst[i]
			res = i
	return res


	### CHAD METHOD ###
	# return min(range(len(lst)), key = lambda i: lst[i])



def arg_max(lst):

	## VIRGIN METHOD ### 
	res = 0
	curr_max = lst[0]
	for i in range(len(lst)):
		if lst[i] > curr_max:
			curr_max = lst[i]
			res = i
	return res

	### CHAD METHOD ###
	# return max(range(len(lst)), key = lambda i: lst[i])




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
	
	print(game1.min_max(1))
	print(game1.min_max(2))
	print(game1.max_min(1))
	print(game1.max_min(2))