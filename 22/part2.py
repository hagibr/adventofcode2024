# input_file = open("22/example2.txt") 
input_file = open("22/input.txt")
input_lines = input_file.readlines()
input_file.close()

secret_list = [int(v) for v in input_lines]

# Optimized next secret calculation
def next(x):
  x = (x ^ (x << 6)) & (0xFFFFFF)
  x = (x ^ (x >> 5)) & (0xFFFFFF)
  x = (x ^ (x << 11)) & (0xFFFFFF)
  return x

# This function generate a dictionary where the key is the tuple of the 4 last changes and
# the value is the first price found with that changes.
# This is going to create a cache of all possibilities for the 2000 first secret numbers
def gen_seqs(start):
  x = start
  price_x1 = x%10
  x = next(x)
  price_x2 = x%10
  x = next(x)
  price_x3 = x%10
  x = next(x)
  price_x4 = x%10
  x = next(x)
  price_x5 = x%10
  seq = dict()
  d1,d2,d3,d4 = price_x2 - price_x1, price_x3 - price_x2, price_x4 - price_x3, price_x5 - price_x4

  for _ in range(2000-4):
    if((d1,d2,d3,d4) not in seq):
      seq[(d1,d2,d3,d4)] = price_x5
    x = next(x)
    price_xn = x%10
    d1 = d2
    d2 = d3
    d3 = d4
    d4 = price_xn - price_x5
    price_x5 = price_xn
    
  return seq

# This will store all the "last 4" changes from all the values from input
all_changes = set()
# This will map the current input value with it's cached values
secret_seq = dict()
for i in secret_list:
  seq = gen_seqs(i)
  # print(i, len(seq))
  secret_seq[i] = seq
  all_changes = all_changes.union(set(seq))
  
print("all", len(all_changes))

# print(1, dict_seq[1].get((-2,1,-1,3),0))
# print(2, dict_seq[2].get((-2,1,-1,3),0))
# print(3, dict_seq[3].get((-2,1,-1,3),0))
# print(2024, dict_seq[2024].get((-2,1,-1,3),0))

max = 0
# Now we test the best sum of all changes
i = 0
for chg in all_changes:
  sum = 0
  for s in secret_list:
    dict_s = secret_seq[s]
    # If we don't find this change on this dictionary, returns 0
    sum += dict_s.get(chg, 0)
  if sum >= max:
    max = sum
    print(max, chg, i)
  i += 1
print(f"Answer: {max}")
