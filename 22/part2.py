input_file = open("22/example2.txt") 
# input_file = open("22/input.txt")
input_lines = input_file.readlines()
input_file.close()

secret_list = [int(v) for v in input_lines]

unique_list = set()
for i in secret_list:
  unique_list.add(i%0xFFFFFF)


# Optimized next secret calculation
def next(x):
  old_x = x
  x = (x ^ (x << 6)) & (0xFFFFFF)
  x = (x ^ (x >> 5)) & (0xFFFFFF)
  x = (x ^ (x << 11)) & (0xFFFFFF)
  return x

def banana2000(x,changes):
  index = 0
  unit_x = x%10
  for i in range(2000):
    x = next(x)
    unit_x2 = x%10
    if( (unit_x2 - unit_x) == changes[index] ):
      index += 1
      if index == len(changes):
        return unit_x2 
    else:
      index = 0
    unit_x = unit_x2
  return 0

# Return all lists of sequences of differences
def seq_price(x,price):
  unit_x = x%10
  x = next(x)
  unit_x2 = x%10
  x = next(x)
  unit_x3 = x%10
  x = next(x)
  unit_x4 = x%10
  d1,d2,d3 = unit_x2 - unit_x, unit_x3 - unit_x2, unit_x4 - unit_x3
  seq = list()
  
  for i in range(2000-3):
    x = next(x)
    unit_xn = x%10
    d4 = unit_xn - unit_x4
    if unit_xn == price:
      seq.append((d1,d2,d3,d4))
    unit_x4 = unit_xn
    d1 = d2
    d2 = d3
    d3 = d4
  return seq

# print(1, banana2000(1,[-2,1,-1,3]))
# print(2, banana2000(2,[-2,1,-1,3]))
# print(3, banana2000(3,[-2,1,-1,3]))
# print(2024, banana2000(2024,[-2,1,-1,3]))

# First we create a set of tuples containing all sequences that give price 9
candidates = set()
for s in secret_list:
  candidates = candidates.union(set(seq_price(s,9)))
print(len(candidates))

max = 0
max2 = 0
# Now we test the best sum of all
count_tests = 0
candidates = list(candidates)
for i in range(len(candidates)):
  sum = 0
  c = candidates[i]
  for s in secret_list:
    sum += banana2000(s, c)
  if sum >= max:
    max = sum
    c_max = c
    print(max, c, c_max, i)
print(f"Answer: {max}")
