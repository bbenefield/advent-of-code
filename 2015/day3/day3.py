import numpy as np

with open('2015/day3/input.txt', 'r') as fin:
    data = fin.readline()

# idx_x = 0
# idx_y = 0

# grid_list = list(data)
# grid_count = len(grid_list) // 2
# grid_arr = np.zeros((grid_count, grid_count))
# grid_arr[idx_x][idx_y] = 1

# for char in grid_list:
#     if char == '^':
#         idx_y += 1
#         grid_arr[idx_x][idx_y] += 1
#     elif char == 'v':
#         idx_y -= 1
#         grid_arr[idx_x][idx_y] += 1
#     elif char == '<':
#         idx_x -= 1
#         grid_arr[idx_x][idx_y] += 1
#     elif char == '>':
#         idx_x += 1
#         grid_arr[idx_x][idx_y] += 1
#     else:
#         continue
    
# print(f'Deliveries made: {np.count_nonzero(grid_arr)}')

class Delivery(object):
    
    def __init__(self, directions):
        self.directions = directions
        self.grid_count = len(list(directions)) // 2
        self.grid = {}
        self.x = 0
        self.y = 0
        self.grid[f'{self.x}:{self.y}'] = 1
        
    def move(self, char):
        if char == '^':
            self.y += 1
        elif char == 'v':
            self.y -= 1
        elif char == '<':
            self.x -= 1
        elif char == '>':
            self.x += 1

        self.grid[f'{self.x}:{self.y}'] = 1
        
    def get_dict(self):
        return self.grid
        
santa = Delivery(data)
robot = Delivery(data)

for idx, char in enumerate(data):
    if idx % 2 == 0:
        santa.move(char)
    else:
        robot.move(char)

santa_dict = santa.get_dict()
robot_dict = robot.get_dict()

final_dict = {**santa_dict, **robot_dict}
      
print(f'Deliveries made: {len(final_dict)}')

#2361
        
