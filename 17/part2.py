# input_file = open("17/example2.txt")
input_file = open("17/input.txt")
input_lines = input_file.readlines()
input_file.close()

# Just parsing
A = B = C = 0
Program = []
for line in input_lines:
  if line.startswith("Register A: "):
    corrupted_A = int(line[12:])
  elif line.startswith("Register B: "):
    initial_B = int(line[12:])
  elif line.startswith("Register C: "):
    initial_C = int(line[12:])
  elif line.startswith("Program: "):
    Program = [int(p) for p in line[9:].split(',')]

# print(A,B,C,Program)

def run_program(value_A, value_B, value_C):
  A, B, C = value_A, value_B, value_C
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
      # Speeding a bit the analysis by comparing the current output with the reference program
      if Program[:len(out)] != out:
        return out # Early exit
      
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
  return out
  
print(Program)
#print(run_program(corrupted_A,initial_B,initial_C))
#print(run_program(117440,initial_B,initial_C))

A = 0
while(True):
  if run_program(A,initial_B,initial_C) == Program:
    break
  A += 1

print(f"Answer: {A}")