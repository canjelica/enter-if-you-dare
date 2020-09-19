import sys

# Mock submission that will return valid path
class ReferenceMazeRunner:
    """Returns a valid path through a maze."""
    
    def __init__(self, maze):
        self.maze = maze
    
    def get_directions():
        """Returns all possible maze directions."""

        all_rooms = list(self.maze.keys())
        exits = []

        for room in rooms:
            exits.extend(list(self.maze[room]['exits']))
            exits = set(exits) #this is to remove duplicates
            exits = tuple(exits) #this is to be able to index into. Is there an advantage to being ordered?
        
        return exits
    def get_rooms()
        """Returns an array of maze rooms."""

        rooms = list(self.maze.keys())
        rooms.remove('start')
        rooms.remove('end')

        return rooms


    def run(self, start, end):

        maze_path = []
    

        return ['West', 'North', 'East', 'East'] #hard coded solution, so this is where I need to write a functino that explores the maze, and returns whatever values the path is. So, start is the dict value i begin with, then chain all the way, checking direction value to see if it matches the end. Once it matches the end, I return that array of saved steps in teh chain
        #Make a list of all the possible directions
        #make a list of all the rooms

class MazeLoader:
    """Implements a maze and maze solver."""

    def __init__(self):
        self.master_list = {}
        
        try:
            #for file in args as f
            #wrapping this in for loop, to the length of args being passed in
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
                
                
                current = self.master_list.get(start)
                #Need to check to make sure the self.master.list[start] is a class object and not just the string "Entrance", same for "Kitchen" and end
                runners = [ReferenceMazeRunner(self.master_list)]
                #Figure out what the def init needs to have, and if it nees to be an array
                for runner in runners:
                    result = runner.run(self.master_list.get(start), self.master_list.get(end))
                    #check to see if end/start are class obejcts, not strings
                    for step in result:
                        current = current.get_square(step)
                        #same check here for class instance
                        if current == None:
                            print('Invalid path returned')
                            break
                    print('Returned ' + ('valid' if self.master_list.get(end).get_name() == current.get_name() else 'invalid') + ' path')
        except FileNotFoundError:
            print('Location of maze file was not found')
        except IOError:
            print('IO Exception reading from maze file')
                

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
