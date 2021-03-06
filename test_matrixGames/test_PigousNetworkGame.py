from game import *
import unittest

game1 = game(2,2)
u1 = [[-1,-1/2],[-1,-1]]
u2 = [[-1,-1], [-1/2,-1]]
nash_equilibria = set([(0,0), (0,1), (1,0)])

class TestNashEquilibria(unittest.TestCase):

	def test_nash_bruteForce(self):
		game1.set_utility_1(u1)
		game1.set_utility_2(u2)

		(z1, z2) = game1.reduced_game_nash()
		self.assertEqual(nash_equilibria, set(game1.nash()))


	def test_nash_elimination(self):
		game1.set_utility_1(u1)
		game1.set_utility_2(u2)

		(z1, z2) = game1.reduced_game_nash()
		reduced_game = game((len(z1)), (len(z2)) )
		reduced_game.set_utility_1(z1)
		reduced_game.set_utility_2(z2)
		self.assertEqual(nash_equilibria, set(reduced_game.nash()))
