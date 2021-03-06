import sys

# Mock submission that will return valid path
class ReferenceMazeRunner:
    def run(self, start, end):
        maze_rooms = deque([("", start)])
        explored = set() 
        
        
        # current_room = current_room.name
        breakpoint()
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
    def __init__(self):
        self.master_list = {}
        
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
                    exits[-1] = exits[-1][:-1] 
                    for exit in exits:
                        direction, next_square = exit.split(':')
                        if next_square not in self.master_list:
                            self.master_list[next_square] = MazeSquare(next_square)
                        square.add_exit(self.master_list.get(next_square), direction)
                start, end = f.readline().split(' ')
                end = end[:-1]
                breakpoint()
                
                current = self.master_list.get(start)
                runners = [ReferenceMazeRunner()]
                for runner in runners:
                    result = runner.run(self.master_list.get(start), self.master_list.get(end))
                    breakpoint()
                    for step in result:
                        current = current.get_square(step)
                        if current == None:
                            print('Invalid path returned')
                            break
                    print('Returned ' + ('valid' if self.master_list.get(end).get_name() == current.get_name() else 'invalid') + ' path')
        except FileNotFoundError:
            print('Location of maze file was not found')
        except IOError:
            print('IO Exception reading from maze file')
                
class MazeSquare:
    def __init__(self, name):
        self.name = name
        self.exits = {}
        
    def add_exit(self, square, direction):                            
        self.exits[direction] = square
    
    def get_name(self):
        return self.name
    
    def get_exists(self):
        return self.exits.keys()
                    
    def get_square(self, direction):
        return self.exits.get(direction, None)                        

MazeLoader()