# input_file = open("15/small_example.txt")
# input_file = open("15/big_example.txt")
input_file = open("15/input.txt")
input_lines = input_file.readlines()
input_file.close()

warehouse = []
moves = []


robot_row, robot_col = 0, 0

row = 0
for line in input_lines:
  if '#' in line:
    warehouse.append([a for a in line.replace('\n', '')])
    if '@' in line:
      robot_row = row
      robot_col = line.index('@')
  elif '^' in line or 'v' in line or '<' in line or '>' in line:
    moves += ([a for a in line.replace('\n', '')])
  row += 1
# for w in warehouse: print(''.join(w)) # Just checking
# print( moves )
# print( robot_row, robot_col )

for m in moves:
  # print(m)
  # Moving up
  if m == '^':
    up_value = warehouse[robot_row-1][robot_col]
    # If the position has a wall, do nothing
    if up_value == '#':
      pass
    # If there's an empty space, just move the robot
    elif up_value == '.':
      warehouse[robot_row][robot_col] = '.'
      robot_row = robot_row-1
      warehouse[robot_row][robot_col] = '@'
    # If there's a box, let's move all the boxes until we find a wall or an empty space
    elif up_value == 'O':

      last_row = robot_row-2
      while( warehouse[last_row][robot_col] == 'O'):
        last_row -= 1
      
      # Is it a wall?
      if warehouse[last_row][robot_col] == '#':
        pass # Do nothing
      # Is it an empty space?
      elif warehouse[last_row][robot_col] == '.':
        # Just put a box there
        warehouse[last_row][robot_col] = 'O'
        # And move up the robot 
        warehouse[robot_row][robot_col] = '.'
        robot_row = robot_row-1
        warehouse[robot_row][robot_col] = '@'
  # Moving down
  if m == 'v':
    down_value = warehouse[robot_row+1][robot_col]
    # If the position has a wall, do nothing
    if down_value == '#':
      pass
    # If there's an empty space, just move the robot
    elif down_value == '.':
      warehouse[robot_row][robot_col] = '.'
      robot_row = robot_row+1
      warehouse[robot_row][robot_col] = '@'
    # If there's a box, let's move all the boxes until we find a wall or an empty space
    elif down_value == 'O':

      last_row = robot_row+2
      while( warehouse[last_row][robot_col] == 'O'):
        last_row += 1
      
      # Is it a wall?
      if warehouse[last_row][robot_col] == '#':
        pass # Do nothing
      # Is it an empty space?
      elif warehouse[last_row][robot_col] == '.':
        # Just put a box there
        warehouse[last_row][robot_col] = 'O'
        # And move down the robot 
        warehouse[robot_row][robot_col] = '.'
        robot_row = robot_row+1
        warehouse[robot_row][robot_col] = '@'

  # Moving left
  if m == '<':
    left_value = warehouse[robot_row][robot_col-1]
    # If the position has a wall, do nothing
    if left_value == '#':
      pass
    # If there's an empty space, just move the robot
    elif left_value == '.':
      warehouse[robot_row][robot_col] = '.'
      robot_col = robot_col-1
      warehouse[robot_row][robot_col] = '@'
    # If there's a box, let's move all the boxes until we find a wall or an empty space
    elif left_value == 'O':

      last_col = robot_col-2
      while( warehouse[robot_row][last_col] == 'O'):
        last_col -= 1
      
      # Is it a wall?
      if warehouse[robot_row][last_col] == '#':
        pass # Do nothing
      # Is it an empty space?
      elif warehouse[robot_row][last_col] == '.':
        # Just put a box there
        warehouse[robot_row][last_col] = 'O'
        # And move left the robot 
        warehouse[robot_row][robot_col] = '.'
        robot_col = robot_col-1
        warehouse[robot_row][robot_col] = '@'   
  
  # Moving right
  if m == '>':
    right_value = warehouse[robot_row][robot_col+1]
    # If the position has a wall, do nothing
    if right_value == '#':
      pass
    # If there's an empty space, just move the robot
    elif right_value == '.':
      warehouse[robot_row][robot_col] = '.'
      robot_col = robot_col+1
      warehouse[robot_row][robot_col] = '@'
    # If there's a box, let's move all the boxes until we find a wall or an empty space
    elif right_value == 'O':

      last_col = robot_col+2
      while( warehouse[robot_row][last_col] == 'O'):
        last_col += 1
      
      # Is it a wall?
      if warehouse[robot_row][last_col] == '#':
        pass # Do nothing
      # Is it an empty space?
      elif warehouse[robot_row][last_col] == '.':
        # Just put a box there
        warehouse[robot_row][last_col] = 'O'
        # And move right the robot 
        warehouse[robot_row][robot_col] = '.'
        robot_col = robot_col+1
        warehouse[robot_row][robot_col] = '@'
  
  # for w in warehouse: print(''.join(w)) # Just checking
  
for w in warehouse: print(''.join(w)) # Just checking

sum_distances = 0

for r in range(1,len(warehouse)):
  for c in range(1, len(warehouse[r])):
    if warehouse[r][c] == 'O':
      sum_distances += 100*r + c

print(f"Answer: {sum_distances}")