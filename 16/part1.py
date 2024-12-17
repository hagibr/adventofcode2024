input_file = open("16/example.txt")
# input_file = open("16/example2.txt")
# input_file = open("16/input.txt")
input_lines = input_file.readlines()
input_file.close()

start_r, start_c = 0, 0
end_r, end_c = 0, 0
for r,line in enumerate(input_lines):
  if 'E' in line:
    end_r, end_c = r, line.index('E')  
  elif 'S' in line:
    start_r, start_c = r, line.index('S')

graph = {}

graph[(start_r, start_c)] = []

# Create all graph connections
def graph_survey(r, c):
  # Get the current node
  n = graph[(r, c)]

  # If the right position is not a wall
  if input_lines[r][c+1] != '#':
    # Add right position to current node
    if (r,c+1) not in n:
      n.append((r,c+1))
    # If there's no node corresponding to this position on graph, create it
    if (r,c+1) not in graph:
      graph[(r,c+1)] = [(r,c)]
      graph_survey(r,c+1)
    # If current position is not on the right node, add it
    elif (r,c) not in graph[(r,c+1)]:
      graph[(r,c+1)].append((r,c)) 
    
  # If the left position is not a wall
  if input_lines[r][c-1] != '#':
    # Add left position to current node
    if (r,c-1) not in n:
      n.append((r,c-1))
    # If there's no node corresponding to this position on graph, create it
    if (r,c-1) not in graph:
      graph[(r,c-1)] = [(r,c)]
      graph_survey(r,c-1)
    # If current position is not on the left node, add it
    elif (r,c) not in graph[(r,c-1)]:
      graph[(r,c-1)].append((r,c)) 
  
  # If the position above is not a wall
  if input_lines[r-1][c] != '#':
    # Add above position to current node
    if (r-1,c) not in n:
      n.append((r-1,c))
    # If there's no node corresponding to this position on graph, create it
    if (r-1,c) not in graph:
      graph[(r-1,c)] = [(r,c)]
      graph_survey(r-1,c)
    # If current position is not on the node above, add it
    elif (r,c) not in graph[(r-1,c)]:
      graph[(r-1,c)].append((r,c)) 
  
  # If the position below is not a wall
  if input_lines[r+1][c] != '#':
    # Add below position to current node
    if (r+1,c) not in n:
      n.append((r+1,c))
    # If there's no node corresponding to this position on graph, create it
    if (r+1,c) not in graph:
      graph[(r+1,c)] = [(r,c)]
      graph_survey(r+1,c)
    # If current position is not on the node above, add it
    elif (r,c) not in graph[(r+1,c)]:
      graph[(r+1,c)].append((r,c)) 

# Create nodes
graph_survey(start_r, start_c)

for n in graph: print(n, graph[n])

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# Starting direction
direction = EAST

