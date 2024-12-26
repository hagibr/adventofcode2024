# input_file = open("25/example.txt")
input_file = open("25/input.txt")
input_lines = input_file.readlines()
input_file.close()

locks = list()
keys = list()

parsing_state = 0 # 0: unknown, 1: lock, 2: key
lock_buffer = None
key_buffer = None

# Converting a lock/key blueprint into an integer
# We basically map a 5x5 grid into a 25 bit integer
for line in input_lines:
  if parsing_state == 0:
    if line == '#####\n':
      parsing_state = 1
      count_steps = 0
      lock_buffer = list()
    elif line == '.....\n':
      parsing_state = 2
      count_steps = 0
      key_buffer = list()
  elif parsing_state == 1:
    if( count_steps < 5 ):
      lock_buffer.append(list(line.strip()))
      count_steps += 1
    else:
      lock_int = 0
      for r, row in enumerate(lock_buffer):
        for c, v in enumerate(row):
          if v == '#':
            lock_int += 1 << (5*c + r)
      locks.append(lock_int)
      parsing_state = 0
  elif parsing_state == 2:
    if( count_steps < 5 ):
      key_buffer.append(list(line.strip()))
      count_steps += 1
    else:
      key_int = 0
      for r, row in enumerate(key_buffer):
        for c, v in enumerate(row):
          if v == '#':
            key_int += 1 << (5*c + r)
      keys.append(key_int)
      parsing_state = 0

print(locks)
print(keys)

# Now it's just a bitwise AND between the list of locks and keys.
fit = 0
for lo in locks:
  for ke in keys:
    # It fits when no bits overlaps, or if the bitwise AND is equal to zero
    if lo & ke == 0:
      fit += 1

print(f"Answer: {fit}")
