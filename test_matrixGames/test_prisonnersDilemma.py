from game import *
import unittest

game1 = game(2,2)
u1 = [[-5,-1],[-10,-2]]
u2 = [[-5,-10], [-1,-2]]
nash_equilibria = set([(0,0)])

class TestNashEquilibria(unittest.TestCase):

	def test_nash_bruteForce(self):
		game1.set_utility_1(u1)
		game1.set_utility_2(u2)
		
		self.assertEqual(nash_equilibria, set(game1.nash_brute_force()))

	def test_nash_2(self):
		game1.set_utility_1(u1)
		game1.set_utility_2(u2)
		self.assertEqual(nash_equilibria, set(game1.nash_method_2()))

	def test_nash_elimination(self):	
		game1.set_utility_1(u1)
		game1.set_utility_2(u2)
		self.assertEqual(nash_equilibria, set(game1.nash_elimination()))

