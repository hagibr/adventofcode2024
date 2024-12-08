# input_file = open("08/example.txt")
input_file = open("08/input.txt")
input_lines = input_file.readlines()
input_file.close()

input_rows = len(input_lines)
input_cols = len(input_lines[0]) - 1

# key: frequency = (0-9a-zA-Z), value = list with coordinates
antenna_map = {}

# Parsing our input
for r in range(input_rows):
  for c in range(input_cols):
    k = input_lines[r][c] 
    if k != '.':
      # Still not in map, so create a new list
      if k not in antenna_map:
        antenna_map[k] = [(r,c)]
      # Already in map, just append to list
      else:
        antenna_map[k].append((r,c))

# print(antenna_map)

# Analyzing or antennas to create an antinode map
antinode_map = {}
for k in antenna_map:
  #print(k)
  antenna_list = antenna_map[k]
  for i in range(len(antenna_list)-1):
    for j in range(i+1,len(antenna_list)):
      A = antenna_list[i]
      B = antenna_list[j]
      #print(A,B)
      # First antinode coordinates
      an_1_r = A[0] + (A[0] - B[0])
      an_1_c = A[1] + (A[1] - B[1])
      # Is it inside the grid?
      if( an_1_r >= 0 and an_1_r < input_rows and an_1_c >= 0 and an_1_c < input_cols):
        an_1 = (an_1_r, an_1_c)
        #print(A,B,an_1)
        if an_1 not in antinode_map:
          antinode_map[an_1] = True
      # Second antinode coordinates
      an_2_r = B[0] + (B[0] - A[0])
      an_2_c = B[1] + (B[1] - A[1])
      # Is it inside the grid?
      if( an_2_r >= 0 and an_2_r < input_rows and an_2_c >= 0 and an_2_c < input_cols):
        an_2 = (an_2_r, an_2_c)
        #print(A,B,an_2)
        if an_2 not in antinode_map:
          antinode_map[an_2] = True

print(f"Answer: {len(antinode_map)}")