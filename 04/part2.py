# input_file = open("04/example.txt")
input_file = open("04/input.txt")
input_lines = input_file.readlines()
input_file.close()

num_rows = len(input_lines)
num_cols = len(input_lines[0])-1 # Discounting new line character

x_mas_count = 0

# There are only 4 patterns:

# M.S   M.M   S.M   S.S
# .A.   .A.   .A.   .A.
# M.S   S.S   S.M   M.M

# Let's give them nicknames:
# MSMS  MMSS  SMSM  SSMM

# So let's just search for the central 'A' and check if the diagonal matches 

# Only one pass, but searching several patterns
for r in range(1,num_rows-1):
  for c in range(1,num_cols-1):
    # Central 'A' found
    if input_lines[r][c] == 'A':
      # MSMS
      if( input_lines[r-1][c-1] == 'M' and input_lines[r-1][c+1] == 'S' and input_lines[r+1][c-1] == 'M' and input_lines[r+1][c+1] == 'S' ):
        x_mas_count += 1
      # MMSS
      elif( input_lines[r-1][c-1] == 'M' and input_lines[r-1][c+1] == 'M' and input_lines[r+1][c-1] == 'S' and input_lines[r+1][c+1] == 'S' ):
        x_mas_count += 1
      # SMSM
      elif( input_lines[r-1][c-1] == 'S' and input_lines[r-1][c+1] == 'M' and input_lines[r+1][c-1] == 'S' and input_lines[r+1][c+1] == 'M' ):
        x_mas_count += 1
      # SSMM
      elif( input_lines[r-1][c-1] == 'S' and input_lines[r-1][c+1] == 'S' and input_lines[r+1][c-1] == 'M' and input_lines[r+1][c+1] == 'M' ):
        x_mas_count += 1


print(f"Answer: {x_mas_count}")