# input_file = open("18/example.txt"); max_r, max_c, max_b = 7, 7, 12
input_file = open("18/input.txt"); max_r, max_c, max_b = 71, 71, 1024
input_lines = input_file.readlines()
input_file.close()

grid = []
for r in range(max_r):
  grid_row = ['.']*(max_c)
  grid.append(grid_row)

for line in input_lines[:max_b]:
  x,y = [int(v) for v in line.strip().split(',')]
  grid[y][x] = '#'

# for grid_row in grid: print(''.join(grid_row))

graph = dict()
for r in range(max_r):
  for c in range(max_c):
    if grid[r][c] == '#':
      continue
    node = set()
    if r-1 >= 0 and grid[r-1][c] != '#':
      node.add((r-1,c))
    if r+1 < max_r and grid[r+1][c] != '#':
      node.add((r+1,c))
    if c-1 >= 0 and grid[r][c-1] != '#':
      node.add((r,c-1))
    if c+1 < max_c and grid[r][c+1] != '#':
      node.add((r,c+1))
    if len(node) > 0:
      graph[r,c] = node

start_node = (0,0)
end_node = (max_r-1,max_c-1)
  
def find_path_to_end():
  visited = []
  to_visit = [(0,0)]

  distances = {}
  for node in graph:
    distances[node] = max_r*max_c

  distances[(0,0)] = 0

  while len(to_visit) > 0:
    node = to_visit[0]
    dist = distances[node]
    for n in to_visit[1:]:
      if distances[n] < dist:
        node = n
        dist = distances[n]
    
    visited.append(node)
    for n in graph[node]:
      if n == end_node:
        return True, visited
      if n in visited:
        continue
      d = dist + 1
      if distances[n] > d:
        distances[n] = d
      if n not in to_visit:
        to_visit.append(n)
    to_visit.remove(node)

  return False, visited

# First we run the path finding with 1024
_, last_visited = find_path_to_end()

answer = None
# Blocking remaining bytes
for line in input_lines[max_b:]:
  c,r = [int(v) for v in line.strip().split(',')]
  
  grid[r][c] = 'X'
  removed = False
  # Removing the node from the graph. First we remove from surround nodes
  if( (r-1,c) in graph ):
    graph[(r-1,c)].remove((r,c))
    removed = True
  if( (r,c-1) in graph ):
    graph[(r,c-1)].remove((r,c))
    removed = True
  if( (r+1,c) in graph ):
    graph[(r+1,c)].remove((r,c))
    removed = True
  if( (r,c+1) in graph ):
    graph[(r,c+1)].remove((r,c))
    removed = True
  # Now we remove from graph
  if (r,c) in graph: graph.pop((r,c))

  # If removing this node doesn't change the graph...
  if not removed:
    print(f"{(c,r)}: doesn't matter")
  # Recalculate a new route only if the previous route was blocked
  elif (r,c) in last_visited:
    print(f"{(c,r)}: rerouting")
    path_found, last_visited = find_path_to_end()
    if not path_found:
      answer = (c,r)
      break
  # If we didn't block the previous node, do not recalculate
  else:
    print(f"{(c,r)}: don't affect last route")

print(f"Answer: {answer}") # I've found 25,6 as answer. It took a long time, maybe a binary search would perform better
for grid_row in grid: print(''.join(grid_row))