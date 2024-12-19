# input_file = open("16/example.txt") # Expected: 7036
# input_file = open("16/example2.txt") # Expected: 11048
input_file = open("16/input.txt") # Expected: 134588 with my input
input_lines = input_file.readlines()
input_file.close()

start_node = (0,0)
end_node = (0,0)
graph = dict()

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# Create all graph nodes and map the start and end nodes
for r, line in enumerate(input_lines):
  for c, v in enumerate(line.strip()):
    if v != '#':
      # Every coordinate generate 4 nodes
      node_north = dict()
      node_east = dict()
      node_south = dict()
      node_west = dict()
      
      # If we can go north
      if input_lines[r-1][c] != '#':
        # Add the north position to north node
        node_north[(r-1,c,NORTH)] = 1
        # Add the possibility to turn to north from east and west node
        node_east[(r,c,NORTH)] = 1000
        node_west[(r,c,NORTH)] = 1000
      # If we can go east
      if input_lines[r][c+1] != '#':
        # Add the east position to east node
        node_east[(r,c+1,EAST)] = 1
        # Add the possibility to turn to east from north and south node
        node_north[(r,c,EAST)] = 1000
        node_south[(r,c,EAST)] = 1000
      # If we can go south  
      if input_lines[r+1][c] != '#':
        # Add the north position to south node
        node_south[(r+1,c,SOUTH)] = 1
        # Add the possibility to turn to south from east and west node
        node_east[(r,c,SOUTH)] = 1000
        node_west[(r,c,SOUTH)] = 1000
      # If we can go west
      if input_lines[r][c-1] != '#':
        # Add the west position to west node
        node_west[(r,c-1,WEST)] = 1
        # Add the possibility to turn to west from north and south node
        node_north[(r,c,WEST)] = 1000
        node_south[(r,c,WEST)] = 1000
      
      # Adding the nodes to graph (even the empty ones)
      graph[(r,c,NORTH)] = node_north
      graph[(r,c,EAST)] = node_east
      graph[(r,c,SOUTH)] = node_south
      graph[(r,c,WEST)] = node_west

    # We always start pointed to EAST  
    if v == 'S':
      start_node = (r,c,EAST)
    # Doesn't matter here which direction, including all
    elif v == 'E':
      end_node = [(r,c,NORTH),(r,c,EAST),(r,c,SOUTH),(r,c,WEST)]
        
# for n in graph: print(n, graph[n])

# These lists are used on Djikstra's algorithm
visited_list = []
to_visit_list = [start_node]

# Initializing the costs of each node (even the empty ones)
cost_list = {}
for g in graph:
  cost_list[g] = -1 # -1 means infinity
# The start node has cost 0
cost_list[start_node] = 0

# print(distances_list)

# Djikstra
while len(to_visit_list) > 0:
  # First we search in the list of "to visit" for the one with lowest cost
  curr_node = to_visit_list[0]
  curr_cost = cost_list[curr_node]
  for n in to_visit_list[1:]:
    if cost_list[n] < curr_cost:
      curr_node = n
      curr_cost = cost_list[n]

  # Get the list of neighbour nodes.
  # The key is the node coordinates (row, column, direction) and the value is the cost
  neighbour_nodes_cost = graph[curr_node]

  # For each neighbour...
  for neighbour in neighbour_nodes_cost:
    # Ignore if this neighbour was already visited
    if neighbour in visited_list:
      continue

    # Get the current distance of the neighbour
    old_distance = cost_list[neighbour]

    # Calculating the new distance if we go from current node
    new_distance = curr_cost + neighbour_nodes_cost[neighbour]

    # Updating the distance
    if old_distance == -1 or new_distance < old_distance:
      cost_list[neighbour] = new_distance
    
    # Adding the node to the "to visit list"
    if neighbour not in end_node and neighbour not in to_visit_list:
      to_visit_list.append(neighbour)
    
  # Moving current node to "visited" list
  to_visit_list.remove(curr_node)
  visited_list.append(curr_node)

# for d in graph: print(d, distances_list[d])

# We have 4 nodes for end coordinates.
# Print them all and select the one with lowest cost, it will reflect the direction where it came from.
for end in end_node:
  print(f"Answer: {cost_list[end]} ({end})")
