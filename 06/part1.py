# input_file = open("06/example.txt")
input_file = open("06/input.txt")
input_lines = input_file.readlines()
input_file.close()

guard_visited_positions = {}

# Current direction
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
direction = -1

row_count = len(input_lines)
col_count = len(input_lines[0])-1

# Current row and column
current_row = -1
current_col = -1

# Searching for start point
for i in range(row_count):
  for j in range(col_count):
    if input_lines[i][j] in ['^', '>', 'v', '<']:
      guard_visited_positions[(i,j)] = True
      direction = ['^', '>', 'v', '<'].index(input_lines[i][j])
      current_row = i
      current_col = j
      break

# Navigating through the map
while True:
  if direction == UP:
    # Where we are going is still inside the map?
    if current_row > 0:
      # Turn right on obstacle
      if input_lines[current_row-1][current_col] == '#':
        direction = RIGHT
      # Go up if not obstacle
      else:
        current_row = current_row - 1
        guard_visited_positions[(current_row,current_col)] = True
    # Going outside of map. Ends here.
    else:
      break
  # Similar analysis for other directions
  elif direction == RIGHT:
    if current_col < col_count - 1:
      if input_lines[current_row][current_col+1] == '#':
        direction = DOWN
      else:
        current_col = current_col + 1
        guard_visited_positions[(current_row,current_col)] = True
    else:
      break
  elif direction == DOWN:
    if current_row < row_count - 1:
      if input_lines[current_row+1][current_col] == '#':
        direction = LEFT
      else:
        current_row = current_row + 1
        guard_visited_positions[(current_row,current_col)] = True
    else:
      break
  elif direction == LEFT:
    if current_col > 0:
      if input_lines[current_row][current_col-1] == '#':
        direction = UP
      else:
        current_col = current_col - 1
        guard_visited_positions[(current_row,current_col)] = True
    else:
      break

# print(current_row, current_col)
print(f"Answer: {len(guard_visited_positions)}")