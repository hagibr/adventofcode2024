# input_file = open("24/example.txt")
# input_file = open("24/example2.txt") 
input_file = open("24/input.txt")
input_lines = input_file.readlines()
input_file.close()


values = dict()
operations = dict()

for line in input_lines:
  if ':' in line:
    name_val = line.strip().split(':')
    name, val = name_val[0], int(name_val[1])
    values[name] = val
  elif "->" in line:
    var_oper = line.strip().split()
    v1, v2, oper, out = var_oper[0], var_oper[2], var_oper[1], var_oper[4]
    if (v1,v2) not in operations:
      operations[(v1,v2)] = []
    operations[(v1,v2)].append((oper,out))

print(values)
print(operations)

while(len(operations) > 0):

  executed = list()

  for (v1,v2) in operations:
    if v1 in values and v2 in values:
      for (oper,out) in operations[(v1,v2)]:
        if oper == "AND":
          values[out] = values[v1] and values[v2]
        elif oper == "OR":
          values[out] = values[v1] or values[v2]
        elif oper == "XOR":
          values[out] = values[v1] ^ values[v2]
        
      executed.append((v1,v2))
  
  for v1v2 in executed:
    operations.pop(v1v2)
      
Z = 0
for v in sorted(values):
  if v[0] == 'z':
    z_val = values[v]
    shift = int(v[1:])
    Z |= z_val << shift
    print(f"{v}: {z_val}")
print(f"Answer: {Z}")