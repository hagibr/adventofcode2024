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
    line = line.replace("#", "##")
    line = line.replace(".", "..")
    line = line.replace("@", "@.")
    line = line.replace("O", "[]")
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

# Check if we can move the current object (robot or box) vertically 
def can_move_vertically(r,c,direction): # direction: -1 (up), +1 (down)
  nr, nc = r+direction, c
  next_w = warehouse[nr][nc]
  # Empty space
  if next_w == '.':
    return True
  # Wall
  elif next_w == '#':
    return False
  # Left side of a box
  elif next_w == '[':
    # Check if can move both sides simultaneally
    return can_move_vertically(nr,nc,direction) and can_move_vertically(nr,nc+1,direction)
  # Right side of a box
  elif next_w == ']':
    # Check if can move both sides simultaneally
    return can_move_vertically(nr,nc,direction) and can_move_vertically(nr,nc-1,direction)

# Move the current object (robot or box) vertically 
def move_vertically(r,c,direction): # direction: -1 (up), +1 (down)
  current_w = warehouse[r][c]
  nr, nc = r+direction, c
  next_w = warehouse[nr][nc]

  # Moving the robot or the box
  if current_w == '@' or current_w == '[' or current_w == ']':
    # If we are pushing the left side of a box
    if next_w == '[':
      # Push it and also push the right side
      move_vertically(nr,nc,direction)
      move_vertically(nr,nc+1,direction)
      # Now moves the current (robot or box) into the next position
      warehouse[nr][nc] = current_w
      # Leaving an empty space
      warehouse[r][c] = '.'
    # If we are pushing the right side of a box
    elif next_w == ']':
      # Push it and also push the left side
      move_vertically(nr,nc,direction)
      move_vertically(nr,nc-1,direction)
      # Now move tue current (robot or box) into the next position
      warehouse[nr][nc] = current_w
      # Leaving an empty space
      warehouse[r][c] = '.'
    # If we are pushing an empty space
    elif next_w == '.':
      # Actually just move the current (robot or box) into this position
      warehouse[nr][nc] = current_w
      # Leaving an empty space
      warehouse[r][c] = '.'
    # Pushing a wall ??? (actually this shouldn't happen)
    elif next_w == '#':
      pass  

# Check if we can move the current object (robot or box) horizontally 
def can_move_horizontally(r,c,direction): # direction: -1 (left), +1 (right)
  nr, nc = r, c+direction
  next_w = warehouse[nr][nc]
  # Next position has an empty space
  if next_w == '.':
    return True
  # Oops, we are going to push a wall
  elif next_w == '#':
    return False
  # OK, box. Check the next position...
  elif next_w == '[' or next_w == ']':
    return can_move_horizontally(nr,nc,direction)

# Move the current object (robot or box) horizontally 
def move_horizontally(r,c,direction): # direction: -1 (left), +1 (right)
  current_w = warehouse[r][c]
  nr, nc = r, c+direction
  next_w = warehouse[nr][nc]
  if current_w == '@' or current_w == '[' or current_w == ']':
    if next_w == '[' or next_w == ']':
      move_horizontally(nr,nc,direction)
      warehouse[nr][nc] = current_w
      warehouse[r][c] = '.'
    elif next_w == '.':
      warehouse[nr][nc] = current_w
      warehouse[r][c] = '.'
    elif next_w == '#':
      pass  

# Now we execute the movements on the robot
for m in moves:
  # print(m)
  # Moving up
  if m == '^':
    if can_move_vertically(robot_row,robot_col,-1):
      move_vertically(robot_row,robot_col,-1)
      robot_row -= 1

  # Moving down
  elif m == 'v':
    if can_move_vertically(robot_row,robot_col,+1):
      move_vertically(robot_row,robot_col,+1)
      robot_row += 1

  # Moving left
  elif m == '<':
    if can_move_horizontally(robot_row,robot_col,-1):
      move_horizontally(robot_row,robot_col,-1)
      robot_col -= 1

  # Moving right
  elif m == '>':
    if can_move_horizontally(robot_row,robot_col,+1):
      move_horizontally(robot_row,robot_col,+1)
      robot_col += 1

  # for w in warehouse: print(''.join(w)) # Just checking
  
# for w in warehouse: print(''.join(w)) # Just checking

sum_distances = 0

for r in range(1,len(warehouse)):
  for c in range(1, len(warehouse[r])):
    if warehouse[r][c] == '[':
      sum_distances += 100*r + c

print(f"Answer: {sum_distances}")