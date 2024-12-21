# input_file = open("20/example.txt"); min_cheat = 2 # 44 
input_file = open("20/input.txt"); min_cheat = 100 # 1411 with my input
input_lines = input_file.readlines()
input_file.close()

grid = [list(row.strip()) for row in input_lines]

# for row in grid: print(''.join(row))

def find_start_end():
  start = None
  end = None
  for r, line in enumerate(grid):
    for c, val in enumerate(line):
      if val == 'S':
        start = (r,c)
        if not end == None:
          return (start,end)
      elif val == 'E':
        end = (r,c)
        if not start == None:
          return (start,end)

start, end = find_start_end()

# Creating the points system: from start to end we just count the number of steps
points = dict()
points[start] = 0
pos = start
p = 1
while(pos != end):
  r,c = pos
  if (r-1,c) not in points and grid[r-1][c] != '#':
    pos = (r-1,c)
  elif (r+1,c) not in points and grid[r+1][c] != '#':
    pos = (r+1,c)
  elif (r,c-1) not in points and grid[r][c-1] != '#':
    pos = (r,c-1)
  elif (r,c+1) not in points and grid[r][c+1] != '#':
    pos = (r,c+1)
  else:
    print("ERROR")
  points[pos] = p
  p += 1

cheat_count = dict()
# These are the offsets that if applied to current position, spend exactly 2 picoseconds
# It's basically the list of points with manhattan distance equal to 2
search_off = [(-2,0), (2,0), (0,2), (0,-2), (-1,-1), (-1,1), (1,-1), (1,1)]
# Now it's time to count the number of cheats that can save at least (min_cheat) picoseconds
for p in points:
  current_points = points[p]
  r,c = p
  # Checks at most 
  for off in search_off:
    p_off = (r+off[0], c+off[1])
    if p_off in points:
      off_points = points[p_off]
      diff = off_points - current_points - 2
      if diff >= min_cheat:
        if diff in cheat_count:
          cheat_count[diff] += 1
        else:
          cheat_count[diff] = 1

for c in sorted(cheat_count): print(f"There is/are {cheat_count[c]} cheat(s) that saves {c} picoseconds.")

sum_cheat = 0
for c in cheat_count:
  sum_cheat += cheat_count[c]
print(f"Answer: {sum_cheat}")
