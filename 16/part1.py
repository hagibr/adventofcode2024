# input_file = open("16/example.txt")
# input_file = open("16/example2.txt")
input_file = open("16/input.txt")
input_lines = input_file.readlines()
input_file.close()

curr_r, curr_c = 0, 0
end_r, end_c = 0, 0
for r,line in enumerate(input_lines):
  if 'E' in line:
    end_r, end_c = r, line.index('E')  
  elif 'S' in line:
    curr_r, curr_c = r, line.index('S')

graph = {}

graph[(curr_r, curr_c)] = {}

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# Our graph_survey is reaching python's default recursion limit of 1000
import sys
sys.setrecursionlimit(10000)

# Create all graph connections
def graph_survey(r, c):
  # Get the current node
  n = graph[(r, c)]

  # If position at EAST is not a wall
  if input_lines[r][c+1] != '#':
    # Add position at EAST to current node
    if (r,c+1) not in n:
      n[(r,c+1)] = EAST
    # If there's no node corresponding to this position on graph, create it and add current node to this new node
    if (r,c+1) not in graph:
      graph[(r,c+1)] = {(r,c):WEST}
      graph_survey(r,c+1)
    # If current position is not in the node, add it
    elif (r,c) not in graph[(r,c+1)]:
      graph[(r,c+1)][(r,c)] = WEST

    
  # If position at WEST is not a wall
  if input_lines[r][c-1] != '#':
    # Add position at WEST to current node
    if (r,c-1) not in n:
      n[(r,c-1)] = WEST
    # If there's no node corresponding to this position on graph, create it and add current node to this new node
    if (r,c-1) not in graph:
      graph[(r,c-1)] = {(r,c):EAST}
      graph_survey(r,c-1)
    # If current position is not in the node, add it
    elif (r,c) not in graph[(r,c-1)]:
      graph[(r,c+1)][(r,c)] = EAST
  
  # If position at NORTH is not a wall
  if input_lines[r-1][c] != '#':
    # Add position at NORTH to current node
    if (r-1,c) not in n:
      n[(r-1,c)] = NORTH
    # If there's no node corresponding to this position on graph, create it and add current node to this new node
    if (r-1,c) not in graph:
      graph[(r-1,c)] = {(r,c):SOUTH}
      graph_survey(r-1,c)
    # If current position is not in the node, add it
    elif (r,c) not in graph[(r-1,c)]:
      graph[(r-1,c)][(r,c)] = SOUTH
  
  # If position at SOUTH is not a wall
  if input_lines[r+1][c] != '#':
    # Add position at SOUTH to current node
    if (r+1,c) not in n:
      n[(r+1,c)] = SOUTH
    # If there's no node corresponding to this position on graph, create it and add current node to this new node
    if (r+1,c) not in graph:
      graph[(r+1,c)] = {(r,c):NORTH}
      graph_survey(r+1,c)
    # If current position is not in the node, add it
    elif (r,c) not in graph[(r+1,c)]:
      graph[(r+1,c)][(r,c)] = NORTH

# Create nodes
graph_survey(curr_r, curr_c)

# for n in graph: print(n, graph[n])

# Starting direction
direction = EAST

visited_list = []
to_visit_list = [(curr_r, curr_c)]

distances_list = {}
distances_list[(curr_r, curr_c)] = (0, EAST)
for g in graph:
  if g != (curr_r, curr_c):
    distances_list[g] = (-1, -1)

# print(distances_list)

current = (curr_r, curr_c)
# Djikstra
while len(to_visit_list) > 0:
  nearest_dist = -1
  # First we search in the list of "to visit" for the nearest
  for n in to_visit_list:
    if nearest_dist == -1 or distances_list[n] < nearest_dist:
      current = n
      nearest_dist = distances_list[n]

  neighbour_list = graph[current]
  for neighbour in neighbour_list:
    # If they haven't been visited before, add them to the visit list
    if neighbour not in visited_list:
      to_visit_list.append(neighbour)

      # Retrieving current node least distance and best direction
      curr_dist, curr_dir = distances_list[current]
      # Retrieving neighbour direction relative to current node
      neighbour_dir = neighbour_list[neighbour]
      # If we have the same direction, the new distance is just one
      if curr_dir == neighbour_dir:
        new_dist = curr_dist + 1
      # If we have to change the direction, the new distance is incremented by 1000
      else:
        new_dist = curr_dist + 1001
      
      # Get the current distance of neighbour
      neigh_dist, _ = distances_list[neighbour]
      # If the new distance is shorter, use this new distance (and update the best distance)
      if neigh_dist == -1 or new_dist < neigh_dist:
        distances_list[neighbour] = (new_dist, neighbour_dir)
  # Moving current node to "visited" list
  to_visit_list.remove(current)
  visited_list.append(current)

print(distances_list)

print(f"Answer: {distances_list[end_r, end_c][0]}")

# 134596: too high
# TODO: use the distances_list to backtrace the shortest path