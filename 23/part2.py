# input_file = open("23/example.txt") 
input_file = open("23/input.txt")
input_lines = input_file.readlines()
input_file.close()

# key: computer name; value: list of connected computers
connections:dict[set] = dict()

computers = set()

intersections:dict[set] = dict()

pairs:list[tuple] = list()
# Parsing the input
for line in input_lines:
  p1, p2 = line.strip().split('-')
  computers.add(p1)
  computers.add(p2)
  this_pair = tuple(sorted([p1,p2]))
  if this_pair not in pairs:
    pairs.append(this_pair)
  if p1 not in connections:
    connections[p1] = set()
  connections[p1].add(p2)
  if p2 not in connections:
    connections[p2] = set()
  connections[p2].add(p1)
  inter = connections[p1].intersection(connections[p2])
  intersections[this_pair] = inter

max_conn = 0
for c in connections:
  if( len(connections[c]) > max_conn ):
    max_conn = len(connections[c])
print(f"There are max {max_conn} connections")

# Let's create some tuples
curr_tuples = pairs
for cardinality in range(3,max_conn+1):
  print(f"Creating all groups of {cardinality}")
  next_tuples:list[list] = list()
  # Checking all current tuples
  for p in curr_tuples:
    # Getting the intersection of the connections of every tuple
    inter = intersections[p]

    for c in inter:
      new_tuple = list(p)[:]
      new_tuple.append(c)
      new_tuple = tuple(sorted(new_tuple))
      if new_tuple not in next_tuples:
        next_tuples.append(new_tuple)
        intersections[new_tuple] = inter.intersection(connections[c])
  print(f"There are {len(next_tuples)} groups")
  if len(next_tuples) > 0:
    curr_tuples = next_tuples


print(','.join(curr_tuples[0]))