import sys
from collections import deque


# Mock submission that will return valid path
class ReferenceMazeRunner:
    """Returns a valid path through a maze."""
    
    def __init__(self, maze):
        self.maze = maze         #this is the self.master_list created in Mazeloader and passed in as parameter

    
    def get_directions():
        """Returns all possible maze directions."""

        all_rooms = list(self.maze.keys())
        exits = []

        for room in rooms:
            exits.extend(list(self.maze[room]['exits']))
            exits = set(exits) #this is to remove duplicates
            exits = tuple(exits) #this is to be able to index into. Is there an advantage to being ordered?
        
        return exits

    def get_rooms():
        """Returns an array of maze rooms."""

        rooms = list(self.maze.keys())
        rooms.remove('start')
        rooms.remove('end') #Does not have the start end keys

        return rooms

    def run(self, start, end):
        """Returns a valid path through a maze using breadth-first search."""
        
        maze_rooms = deque([("", start)])
        explored = set() 
        
        
        while maze_rooms:
            path, current_room = maze_rooms.popleft()
            current_room = current_room.name
            possible_exits = self.maze[current_room].exits
            
            if current_room == end:
                return path

            for direction, next_room in possible_exits.items():
                breakpoint()
                if not next_room in explored:
                    maze_rooms.append(([path, direction], next_room))
            
            explored.add(current_room)
            
        


class MazeLoader:
    """Implements a maze and maze solver."""

    def __init__(self):
        self.master_list = {}

        try:
            with open(sys.argv[1], 'r') as f:

                # Begin reading file line-by-line
                cell_nums = int(f.readline())

                # Variableizes elements of each line
                for _ in range(cell_nums):
                    curr_line = f.readline()
                    parts = curr_line.split(' ', 2)
                    name = parts[0]
                    # Adding MazeSquare object to dictionary by maze room name
                    if name not in self.master_list:
                        self.master_list[name] = MazeSquare(name)
                    
                    # Create variables for 
                    square = self.master_list.get(name)
                    doors = parts[1].split(',') #list of direction:room elements
                    doors[-1] = doors[-1][:-1]
                    
                    for door in doors: 
                        direction, next_square = door.split(':')

                        if next_square not in self.master_list:
                            self.master_list[next_square] = MazeSquare(next_square) #change to str not object

                        square.add_exit(next_square, direction)
                

                #Adding start, end variables as strings
                start, end = f.readline().split(' ')
                breakpoint()
            current_room = self.master_list.get(start) # This is a MazeSquare object
            runners = [ReferenceMazeRunner(self.master_list)] 

            for runner in runners:
                # This returns an array with a valid maze path through given maze
                result = runner.run(self.master_list.get(start), self.master_list.get(end))

                for step in result:
                    current_room = current_room.get_square(step) 

                    if current_room == None:
                        print('Invalid path returned')
                        break

                if current_room == end: 
                    print('Returned ' + ('valid' if self.master_list.get(end).get_name() == current_room.get_name() else 'invalid') + ' path')

        except FileNotFoundError:
            print('Location of maze file was not found')
        except IOError:
            print('IO Exception reading from maze file')

class MazeSquare:
    """Implements a room in a maze."""

    def __init__(self, name):
        self.name = name
        self.exits = {}
    
    def __repr__(self):
        return f"< {self.name} >" 
        
    def add_exit(self, square, direction):                            
        self.exits[direction] = square
    
    def get_name(self):
        return self.name
    
    def get_exits(self):
        return self.exits.keys()
                    
    def get_square(self, direction):
        return self.exits.get(direction, None)                        

MazeLoader()





#class broken up into inidiidual units of work, unit tests are testing each of those units
#break up def init in Maze Loader to separate it out
#patter for unite test
# Arrange
# Act
# Assert



#1. Clean up Maze Loader
#2. Look for Units to test
#3. Clean up readability, put all comments and areas for improvement below in text#
#4. Write test stubs
#5. Put notes together
#6. Work on webapp