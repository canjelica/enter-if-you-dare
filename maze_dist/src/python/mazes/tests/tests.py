#Arrange--get data
#Act--call methods
#Assert

# TDD, fixing bugs
# write a unit test around bug showing that it failed, fix the code until it passed


#---------------Unit Tests---------------#
import unittest

from MazeLoader import MazeRunner
#Unit test to return populated self.master_list


class TestMazeLoader(unittest.TestCase):
	#Unit test to make sure dictionary of possible exits is being pulled successfully from self.maze
# Arrange: Initialize maze
# MazeLoader() with simple.maze sys.argv, need to break out this method in MazeLoader

#Act: Call method

#Assert


class TestRun(unittest.TestCase):
	def test_run(self):
		"""Test that run function can return an array with valid path."""

		# Don't know whether to hardcode dictionary or pull from MazeLoader
		maze = {'Entrance': {'name':'Entrance', 'exits': {'North': 'Hall',				'East':'Dining','West':'Sitting'}},

						'Hall': {'name': 'Hall', 'exits': {'South':'Entrance','East':'Kitchen','West':'Bedroom'}},
						
						'Dining': {'name':'Dining', 'exits': {'North':'Kitchen','West':'Entrance'}},
						
						'Sitting': {'name': 'Sitting', 'exits': {'North':'Bedroom','East':'Entrance'}},
						
						'Kitchen': {'name': 'Kitchen', 'exits': { 'West':'Hall', 'South':'Dining'}},
						
						'Bedroom': {'name': 'Bedroom', 'exits': {'East':'Hall','South':'Sitting'}},

						'start': 'Entrance',

						'end': 'Kitchen'}
		result = [['North', 'East'], ['East', 'North'], ['West', 'North', 'East', 'East']] #How to add in all possible solutions?
		
		self.assertEqual() #check to see if in result

		if __name__ == '__main__':
			unittest.main()

		