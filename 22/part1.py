# input_file = open("22/example.txt") 
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

def next2000(x):
  for i in range(2000):
    x = next(x)
  return x

sum = 0
for s in secret_list:
  sum += next2000(s)

print(f"Answer: {sum}")
