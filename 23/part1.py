# input_file = open("23/example.txt") 
input_file = open("23/input.txt")
input_lines = input_file.readlines()
input_file.close()

# key: computer name; value: list of connected computers
connections = dict()

# Parsing the input
for line in input_lines:
  p1, p2 = line.strip().split('-')
  if p1 not in connections:
    connections[p1] = [p2]
  else:
    connections[p1].append(p2)
  if p2 not in connections:
    connections[p2] = [p1]
  else:
    connections[p2].append(p1)

# Checking the computers connected in triangles (p1 connected to p2, p2 connected to p3, p3 connected to p1)
triangles = list()
count_t = 0
# Search for all triangles
for p1 in connections:
  c1 = connections[p1]
  for p2 in c1:
    c2 = connections[p2]
    for p3 in c2:
      # Can't be the same as p1
      if p3 != p1:
        if p1 in connections[p3]:
          # Sorting the computers by name just to have a unique entry
          p1p2p3 = sorted([p1,p2,p3])
          if(p1p2p3 not in triangles):
            triangles.append(p1p2p3)
            # If at least one of the computers have 't' at the start...
            if p1[0] == 't' or p2[0] == 't' or p3[0] == 't':
              count_t += 1
              print(p1p2p3)

print(f"Answer: {count_t}")