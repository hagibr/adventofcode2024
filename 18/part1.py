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
visited = []
to_visit = [(0,0)]

distances = {}
for node in graph:
  distances[node] = max_r*max_c

distances[(0,0)] = 0
previous = dict()

while len(to_visit) > 0:
  node = to_visit[0]
  dist = distances[node]
  for n in to_visit[1:]:
    if distances[n] < dist:
      node = n
      dist = distances[n]
  
  for n in graph[node]:
    if n in visited:
      continue
    d = dist + 1
    if distances[n] > d:
      distances[n] = d
      previous[n] = node
    
    if n not in to_visit:
      to_visit.append(n)

  visited.append(node)
  to_visit.remove(node)

print(f"Answer: {distances[end_node]}")

node = end_node
while( node != start_node ):
  grid[node[0]][node[1]] = 'O'
  node = previous[node]

for grid_row in grid: print(''.join(grid_row))