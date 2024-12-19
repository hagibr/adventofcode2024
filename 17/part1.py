# input_file = open("17/example.txt")
input_file = open("17/input.txt")
input_lines = input_file.readlines()
input_file.close()

# Just parsing
A = B = C = 0
Program = []
for line in input_lines:
  if line.startswith("Register A: "):
    A = int(line[12:])
  elif line.startswith("Register B: "):
    B = int(line[12:])
  elif line.startswith("Register C: "):
    C = int(line[12:])
  elif line.startswith("Program: "):
    Program = [int(p) for p in line[9:].split(',')]

# print(A,B,C,Program)

out = []
# Let's process
ip = 0
while(ip < len(Program)):
  opcode = Program[ip]
  literal = Program[ip+1]
  combo = 0
  if 0 <= literal <= 3:
    combo = literal
  elif literal == 4:
    combo = A
  elif literal == 5:
    combo = B
  elif literal == 6:
    combo = C
  
  # adv
  if opcode == 0:
    A = A >> combo
  # bxl
  elif opcode == 1:
    B = B ^ literal
  # bst
  elif opcode == 2:
    B = combo % 8
  # jnz
  elif opcode == 3:
    if A != 0:
      ip = literal
      continue
  # bxc
  elif opcode == 4:
    B = B ^ C
  # out
  elif opcode == 5:
    out.append(combo % 8)
  # bdv
  elif opcode == 6:
    B = A >> combo
  # cdv
  elif opcode == 7:
    C = A >> combo
  # invalid???
  else:
    print(f"Invalid opcode: {opcode}")
  # next instruction...
  ip += 2
  
print(f"Answer: {','.join([str(v) for v in out])}")