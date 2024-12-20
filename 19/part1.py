# input_file = open("19/example.txt")
input_file = open("19/input.txt")
input_lines = input_file.readlines()
input_file.close()

patterns = input_lines[0].strip().split(', ')

print(patterns)

def find_pattern(where):
  if len(where) == 0:
    return True
  for p in patterns:
    if where == p:
      return True
    elif where.startswith(p):
      if find_pattern(where[len(p):]):
        return True
  return False

possible = 0
for line in input_lines[2:]:
  line = line.strip()
  if find_pattern(line):
    print(f"{line}: OK")
    possible += 1
  else:
    print(f"{line}: NOT OK")

print(f"Answer: {possible}")