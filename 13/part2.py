# input_file = open("13/example.txt")
input_file = open("13/input.txt")
input_lines = input_file.readlines()
input_file.close()

machines = []

# Parsing the lines into arrays of 6 elements
AX, AY, BX, BY, PX, PY = 0, 0, 0, 0, 0, 0
for line in input_lines:
  if line.startswith("Button A"):
    line_A = line.split()
    AX = int(line_A[2][2:-1])
    AY = int(line_A[3][2:])
  elif line.startswith("Button B"):
    line_B = line.split()
    BX = int(line_B[2][2:-1])
    BY = int(line_B[3][2:])
  elif line.startswith("Prize"):
    line_P = line.split()
    # This is the only differences between part1 and part2
    PX = int(line_P[1][2:-1]) + 10000000000000
    PY = int(line_P[2][2:]) + 10000000000000
    machines.append([AX, AY, BX, BY, PX, PY])

tokens = 0

# Px = a*Ax + b*Bx
# Py = a*Ay + b*By
# Now we are going to use the Kramer's rule
# D = det |Ax Bx|
#         |Ay By|
# Da = det |Px Bx|
#          |Py By|
# Db = det |Ax Px|
#          |Ay Py|
# a = Da/D
# b = Db/D
# a and b must be integers
for ma in machines:
  AX, AY, BX, BY, PX, PY = ma
  D = AX*BY - AY*BX
  Da = PX*BY - PY*BX
  Db = PY*AX - PX*AY
  if D == 0:
    print(f"{ma}: impossible")
  else:
    a = Da/D
    b = Db/D
    print(f"{ma}: a = {a}, b = {a}")
    if a == int(a) and b == int(b):
      tokens += 3*int(a) + int(b)
  
print(f"Answer: {tokens}")