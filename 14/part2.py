input_file = open("14/input.txt")
input_lines = input_file.readlines()
input_file.close()

# Input
cols, rows = 101, 103

# Robot list
robots = []

# Create empty space
space = []
for r in range(rows):
  space.append([0]*cols)

# Parsing input for robots and fill the space
for line in input_lines:
  p, v = line.split()
  px,py = [int(a) for a in p[2:].split(',')]
  vx,vy = [int(a) for a in v[2:].split(',')]
  robots.append([px,py,vx,vy])
  space[py][px] += 1

# Now is the good part of part 2
seconds = 0
while(True):
  print(f"Seconds: {seconds}")

  # Cheating a bit here, because I've seen at Reddit that the tree is inside a rectangular frame
  maybe = False # This is our flag that indicates that maybe we've found a solution
  for r in range(rows):
    count_seq = 0
    for c in range(cols):
      if(space[r][c] > 0):
        count_seq += 1
        # Our trigger is a sequence of at least 10 robots inline
        if( count_seq > 10 ):
          maybe = True
          break
      else:
        count_seq = 0
    if maybe:
      break
  
  # Checking the solution
  if maybe:
    # Print the space
    for r in range(rows):
      for c in range(cols):
        if(space[r][c] > 0):
          print('#', end='')
        else:
          print(' ', end='')
      print()
    # Waits for user input
    command = input()
  
  # Move the robots to next position
  for r in range(len(robots)):
    px, py, vx, vy = robots[r]
    space[py][px] -= 1
    px = (px + vx) % cols
    py = (py + vy) % rows
    space[py][px] += 1
    robots[r] = [px, py, vx, vy]
    
  # Advancing the time
  seconds += 1
