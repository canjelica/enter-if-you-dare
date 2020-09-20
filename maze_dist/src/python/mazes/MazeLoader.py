import sys
from collections import deque

# Mock submission that will return valid path
class ReferenceMazeRunner:
    """Returns a valid path through a maze."""
    
    def __init__(self, maze):
        self.maze = maze  #This has the start end keys
    
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
        """Returns a valid path through a maze."""

        maze = self.maze 

        maze_rooms = [("", start)] ##make into a deque after, Return index into with arr[i][0]
        explored = set() #(start, Hall, Dining, Sitting)
        maze_path = [North, East,West]
        
        while maze_rooms:
            path, current_room = maze_rooms.popleft()
            # path = North South
            #current_room = Entrance
            maze_path.extend(path)

            possible_exits = maze[current_room].get('exits')) #'North':'Bedroom','East':'Entrance'}

            if current_room in explored:
                continue
            
            for direction, next_room in possible_exits.items():
                maze_rooms.extend(((path,direction), next_room))  #[ (North East Kitchen),(North West Bedroom), (East, North Kitchen), East, WEst Entrance), (West North Bedroom), (WEst East Entrance) ]
                
                # OPTIMIZE: if path if followed by opposite direction, remove path as one to explore, perhaps separate function

            if current_room = end:
                maze_path = path
                return maze_path

            explored.add(current_room)


class MazeLoader:
    """Implements a maze and maze solver."""

    def __init__(self):
        self.master_list = {}

        def read_maze_file()
            """Returns a dictionary of maze rooms."""
            
            try:
                with open(sys.argv[1], 'r') as f:
                    cell_nums = int(f.readline())

                    for _ in range(cell_nums):
                        curr_line = f.readline()
                        parts = curr_line.split(' ', 2)
                        name = parts[0]

                        if name not in self.master_list:
                            self.master_list[name] = MazeSquare(name)
                        
                        square = self.master_list.get(name)
                        exits = parts[1].split(',')

                        for exit in exits: #is exit a reserved keyword?
                            direction, next_square = exit.split(':')

                            if next_square not in self.master_list:
                                self.master_list[next_square] = MazeSquare(next_square)
                            square.add_exit(self.master_list.get(next_square), direction)

                    start, end = f.readline().split(' ')
                    #maybe a bug here with how it's saving start, end. End not getting a value? Debug.

            except FileNotFoundError:
                print('Location of maze file was not found')
            except IOError:
                print('IO Exception reading from maze file')
            
            def check_maze_run():
                """Checks to see if maze run was a valid path."""

                current = self.master_list.get(start) #Room object
                    #Need to check to make sure the self.master.list[start] is a class object and not just the string "Entrance", same for "Kitchen" and end
                    runners = [ReferenceMazeRunner(self.master_list)]
                    #Figure out what the def init needs to have, and if it nees to be an array

                    for runner in runners:
                        result = runner.run(self.master_list.get(start), self.master_list.get(end))
                        #check to see if end/start are class obejcts, not strings

                        for step in result: #North, East
                            current = current.get_square(step) #throws in run returned first direction, and returns the room at the direction, or None if it doesn't exist
                            #same check here for class instance

                            if current == None:
                                print('Invalid path returned')
                                break

                        if current == end: #There is a bug here, somehow getting None from get_square function
                            print('Returned ' + ('valid' if self.master_list.get(end).get_name() == current.get_name() else 'invalid') + ' path')


class MazeSquare:
    """Implements a room in a maze."""

    def __init__(self, name):
        self.name = name
        self.exits = {}
        
    def add_exit(self, square, direction):                            
        self.exits[direction] = square
    
    def get_name(self):
        return self.name
    
    def get_exits(self):
        return self.exits.keys()
                    
    def get_square(self, direction):
        return self.exits.get(direction, None)                        

# MazeLoader()





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