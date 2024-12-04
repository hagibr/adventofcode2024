# input_file = open("04/example.txt")
input_file = open("04/input.txt")
input_lines = input_file.readlines()
input_file.close()

num_rows = len(input_lines)
num_cols = len(input_lines[0])-1 # Discounting new line character

xmas_count = 0

# Horizontal search
for r in range(num_rows):
  for c in range(num_cols-3):
    if input_lines[r][c] == 'X' and input_lines[r][c+1] == 'M' and input_lines[r][c+2] == 'A' and input_lines[r][c+3] == 'S':
      xmas_count += 1
    elif input_lines[r][c] == 'S' and input_lines[r][c+1] == 'A' and input_lines[r][c+2] == 'M' and input_lines[r][c+3] == 'X':
      xmas_count += 1

# Vertical search
for r in range(num_rows-3):
  for c in range(num_cols):
    if input_lines[r][c] == 'X' and input_lines[r+1][c] == 'M' and input_lines[r+2][c] == 'A' and input_lines[r+3][c] == 'S':
      xmas_count += 1
    elif input_lines[r][c] == 'S' and input_lines[r+1][c] == 'A' and input_lines[r+2][c] == 'M' and input_lines[r+3][c] == 'X':
      xmas_count += 1

# Diagonal \ search
for r in range(num_rows-3):
  for c in range(num_cols-3):
    if input_lines[r][c] == 'X' and input_lines[r+1][c+1] == 'M' and input_lines[r+2][c+2] == 'A' and input_lines[r+3][c+3] == 'S':
      xmas_count += 1
    elif input_lines[r][c] == 'S' and input_lines[r+1][c+1] == 'A' and input_lines[r+2][c+2] == 'M' and input_lines[r+3][c+3] == 'X':
      xmas_count += 1

# Diagonal / search
for r in range(3,num_rows):
  for c in range(num_cols-3):
    if input_lines[r][c] == 'X' and input_lines[r-1][c+1] == 'M' and input_lines[r-2][c+2] == 'A' and input_lines[r-3][c+3] == 'S':
      xmas_count += 1
    elif input_lines[r][c] == 'S' and input_lines[r-1][c+1] == 'A' and input_lines[r-2][c+2] == 'M' and input_lines[r-3][c+3] == 'X':
      xmas_count += 1

print(f"Answer: {xmas_count}")