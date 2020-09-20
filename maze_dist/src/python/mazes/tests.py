#Arrange--get data
#Act--call methods
#Assert

#TDD, fixing bugs
#write a untie test around bug showing that it failed, fix the code until it passed


#---------------Unit Tests---------------#

#Unit test to return populated self.master_list
# Arrange
# Act
# Assert




#Unit test to make sure dictionary of possible exits is being pulled successfully from self.maze

# Arrange: Initialize maze
# MazeLoader() with simpe.maze sys.argv, need to break out this method in MazeLoader
# 
possible_exits = maze[current_room].get('exits')) 

#{'North': 'Hall','East':'Dining','West':'Sitting'}

#Act: Call method

#Assert