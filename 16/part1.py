# input_file = open("16/example.txt")
# input_file = open("16/example2.txt")
input_file = open("16/input.txt")
input_lines = input_file.readlines()
input_file.close()

start_node = (0,0)
end_node = (0,0)
graph = {}

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# Create all graph nodes and map the start and end nodes
for r, line in enumerate(input_lines):
  for c, v in enumerate(line.replace('\n','')):
    if v != '#':
      node = {}
      if input_lines[r+1][c] != '#':
        node[(r+1,c)] = SOUTH
      if input_lines[r][c-1] != '#':
        node[(r,c-1)] = WEST
      if input_lines[r][c+1] != '#':
        node[(r,c+1)] = EAST
      if input_lines[r-1][c] != '#':
        node[(r-1,c)] = NORTH
      graph[(r,c)] = node
    if v == 'S':
      start_node = (r, c)
    elif v == 'E':
      end_node = (r, c)
        
# for n in graph: print(n, graph[n])

# Starting direction
direction = EAST

visited_list = []
to_visit_list = [start_node]

distances_list = {}
distances_list[start_node] = (0, EAST)
for g in graph:
  if g != (start_node):
    distances_list[g] = (-1, -1)

# print(distances_list)

curr_node = start_node

# Djikstra
while len(to_visit_list) > 0:
  nearest_dist = -1
  # First we search in the list of "to visit" for the nearest
  for n in to_visit_list:
    if nearest_dist == -1 or distances_list[n] < nearest_dist:
      curr_node = n
      nearest_dist = distances_list[n]

  neighbour_list = graph[curr_node]
  for neighbour in neighbour_list:
    # If they haven't been visited before OR if we can give a better distance
    if neighbour not in visited_list:
      # This can re-add an already visited node, because of the second condition above
      to_visit_list.append(neighbour)

      # Retrieving current node least distance and best direction
      curr_dist, curr_dir = distances_list[curr_node]
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
      if neigh_dist == -1 or new_dist <= neigh_dist:
        distances_list[neighbour] = (new_dist, neighbour_dir)
        


  # Moving current node to "visited" list
  to_visit_list.remove(curr_node)
  if curr_node not in visited_list:
    visited_list.append(curr_node)

# for d in graph: print(d, distances_list[d])

print(f"Answer: {distances_list[end_node][0]}")

debug_map = []
for line in input_lines:
  debug_line = []
  for c in line.replace('\n','').replace('.', ' '):
    debug_line.append(c)
  debug_map.append(debug_line)

curr_node = end_node
while( curr_node != start_node ):
  d = curr_node
  if distances_list[d][1] == NORTH:
    debug_map[d[0]][d[1]] = '@'
    curr_node = (d[0]+1, d[1])
  elif distances_list[d][1] == SOUTH:
    debug_map[d[0]][d[1]] = '@'
    curr_node = (d[0]-1, d[1])
  elif distances_list[d][1] == EAST:
    debug_map[d[0]][d[1]] = '@'
    curr_node = (d[0], d[1]-1)
  elif distances_list[d][1] == WEST:
    debug_map[d[0]][d[1]] = '@'
    curr_node = (d[0], d[1]+1)
  
# for line in debug_map:
#   print(''.join(line))

for d in distances_list:
  if distances_list[d][1] == NORTH:
    debug_map[d[0]][d[1]] = '^'
  elif distances_list[d][1] == SOUTH:
    debug_map[d[0]][d[1]] = 'v'
  elif distances_list[d][1] == EAST:
    debug_map[d[0]][d[1]] = '>'
  elif distances_list[d][1] == WEST:
    debug_map[d[0]][d[1]] = '<'

# for line in debug_map:
#   print(''.join(line))

# 134596: too high
# TODO: use the distances_list to backtrace the shortest path
# The shortest path discounting the 90 degree cost is 504
# Using friend's code, the result was 134588, let's try to reach this magic value
# My mistake: compute the distance including the 90 degree cost, but we can't include it yet
# Maybe the best approach is calculate every path and then choose the shortest