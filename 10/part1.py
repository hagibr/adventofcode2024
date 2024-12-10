# input_file = open("10/example.txt")
input_file = open("10/input.txt")
input_lines = input_file.readlines()
input_file.close()

input_rows = len(input_lines)
input_cols = len(input_lines[0]) - 1

trail_scores = {}

# Map string of digits to list of integers
input_data = []
for line in input_lines:
  input_data.append([int(v) for v in line[:input_cols]])

# Recursive trail seeking
def wander_trail(start, current):
  row, col = current
  val_current = input_data[row][col]
  if val_current == 9:
    if current not in trail_scores[start]:
      trail_scores[start].append(current)
    return
  
  if row > 0:
    val_up = input_data[row-1][col]
    if (val_up - val_current) == 1:
      wander_trail(start, (row-1, col))
  if row < input_rows-1:
    val_down = input_data[row+1][col]
    if (val_down - val_current) == 1:
      wander_trail(start, (row+1, col))
  if col > 0:
    val_left = input_data[row][col-1]
    if (val_left - val_current) == 1:
      wander_trail(start, (row, col-1))
  if col < input_cols-1:
    val_right = input_data[row][col+1]
    if (val_right - val_current) == 1:
      wander_trail(start, (row, col+1))

for r in range(input_rows):
  for c in range(input_cols):
    if input_data[r][c] == 0:
      trail_scores[(r,c)] = []
      wander_trail((r,c), (r,c))

sum_scores = 0
for t in trail_scores:
  sum_scores += len(trail_scores[t])
  #print(t, trail_scores[t])

print(f"Answer: {sum_scores}")