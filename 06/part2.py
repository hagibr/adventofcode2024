# input_file = open("06/example.txt")
input_file = open("06/input.txt")
input_lines = input_file.readlines()
input_file.close()

# Current direction
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

row_count = len(input_lines)
col_count = len(input_lines[0])-1

# This is the matrix (list of lists) to be used instead of the list of lines (strings)
input_data = []

# Searching for start point
for i in range(row_count):
  input_data.append(list(input_lines[i][:col_count]))
  for j in range(col_count):
    if input_lines[i][j] in ['^', '>', 'v', '<']:
      starting_direction = ['^', '>', 'v', '<'].index(input_lines[i][j])
      starting_row = i
      starting_col = j
      break

# print(input_data)

# This function returns True when the current map have a loop and False otherwise
def is_loop():
  direction = starting_direction
  current_row = starting_row
  current_col = starting_col
  guard_visited_positions = {}
  guard_visited_positions[(current_row, current_col)] = True

  # This is our loop detection: stores every coordinates where we turned right. If it's already stored, we found a loop.
  turn_right_positions = {}
  # Navigating through the map
  while True:
    if direction == UP:
      # Where we are going is still inside the map?
      if current_row > 0:
        # Turn right on obstacle
        if input_data[current_row-1][current_col] == '#':
          direction = RIGHT
          # Loop detected?
          if( (current_row, current_col) in turn_right_positions ):
            return True
          else:
            turn_right_positions[(current_row, current_col)] = True
        # Go up if not obstacle
        else:
          current_row = current_row - 1
          guard_visited_positions[(current_row,current_col)] = True
      # Going outside of map. Ends here.
      else:
        return False
    # Similar analysis for other directions
    elif direction == RIGHT:
      if current_col < col_count - 1:
        if input_data[current_row][current_col+1] == '#':
          direction = DOWN
        else:
          current_col = current_col + 1
          guard_visited_positions[(current_row,current_col)] = True
      else:
        return False
    elif direction == DOWN:
      if current_row < row_count - 1:
        if input_data[current_row+1][current_col] == '#':
          direction = LEFT
        else:
          current_row = current_row + 1
          guard_visited_positions[(current_row,current_col)] = True
      else:
        return False
    elif direction == LEFT:
      if current_col > 0:
        if input_data[current_row][current_col-1] == '#':
          direction = UP
        else:
          current_col = current_col - 1
          guard_visited_positions[(current_row,current_col)] = True
      else:
        return False

# Now we do an exaustive analysis
count_loops = 0
for i in range(row_count):
  for j in range(col_count):
    # Free space?
    if input_data[i][j] == '.':
      # Put an obstacle
      input_data[i][j] = '#'
      # If we find a loop, increment the counter
      if( is_loop() ):
        count_loops += 1
      # Remove the obstacle to preserve the original map
      input_data[i][j] = '.'

print(f"Answer: {count_loops}")