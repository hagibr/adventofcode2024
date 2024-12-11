# input_file = open("11/example.txt")
input_file = open("11/input.txt")
input_line = input_file.readline()
input_file.close()

initial = [int(v) for v in input_line.split()]

# print(initial)

count_stones = [0]

def blink(blink_times, value):
  if blink_times == 25:
    count_stones[0] = count_stones[0] + 1
    return
  
  str_value = str(value)
  if value == 0:
    blink(blink_times+1, 1)
  elif len(str_value) % 2 == 0:
    left = int(str_value[:len(str_value)//2])
    right = int(str_value[len(str_value)//2:])
    blink(blink_times+1, left)
    blink(blink_times+1, right)
  else:
    blink(blink_times+1, value*2024)

for v in initial:
  blink(0,v)

print(f"Answer: {count_stones[0]}")