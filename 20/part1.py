# input_file = open("20/example.txt"); min_cheat = 2
input_file = open("20/input.txt"); min_cheat = 100
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
# Now it's time to count the number of cheats that can save at least 100 picoseconds
for r, line in enumerate(grid):
  for c, val in enumerate(line):
    # Checking every wall
    if val == '#':
      # Calculing the sides
      north = (r-1,c)
      south = (r+1,c)
      east = (r,c+1)
      west = (r,c-1)
      # Now we test if there are 2 sides with differences of points of at least 102
      # This is because when we cheat, we consume 2 points, so the total saved will
      # be at least 100 points 
      if( north in points ):
        points_north = points[north]
        if( south in points ):
          diff_points = abs(points_north - points[south]) - 2
          if( diff_points >= min_cheat ):
            if diff_points in cheat_count:
              cheat_count[diff_points] += 1
            else:
              cheat_count[diff_points] = 1
        if( east in points ):
          diff_points = abs(points_north - points[east]) - 2
          if( diff_points >= min_cheat ):
            if diff_points in cheat_count:
              cheat_count[diff_points] += 1
            else:
              cheat_count[diff_points] = 1
        if( west in points ):
          diff_points = abs(points_north - points[west]) - 2
          if( diff_points >= min_cheat ):
            if diff_points in cheat_count:
              cheat_count[diff_points] += 1
            else:
              cheat_count[diff_points] = 1
      if( south in points ):
        points_south = points[south]
        if( east in points ):
          diff_points = abs(points_south - points[east]) - 2
          if( diff_points >= min_cheat ):
            if diff_points in cheat_count:
              cheat_count[diff_points] += 1
            else:
              cheat_count[diff_points] = 1
        if( west in points ):
          diff_points = abs(points_south - points[west]) - 2
          if( diff_points >= min_cheat ):
            if diff_points in cheat_count:
              cheat_count[diff_points] += 1
            else:
              cheat_count[diff_points] = 1
      if( east in points ):
        if( west in points ):
          diff_points = abs(points[east] - points[west]) - 2
          if( diff_points >= min_cheat ):
            if diff_points in cheat_count:
              cheat_count[diff_points] += 1
            else:
              cheat_count[diff_points] = 1

for c in sorted(cheat_count): print(f"There is/are {cheat_count[c]} cheat(s) that saves {c} picoseconds.")

sum_cheat = 0
for c in cheat_count:
  sum_cheat += cheat_count[c]
print(f"Answer: {sum_cheat}")
