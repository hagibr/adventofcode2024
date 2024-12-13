# input_file = open("11/example.txt")
input_file = open("11/input.txt")
input_line = input_file.readline()
input_file.close()

initial = [int(v) for v in input_line.split()]

def blink(blink_times, value):
  if blink_times == 25:
    return 1
  
  str_value = str(value)
  if value == 0:
    return blink(blink_times+1, 1)
  elif len(str_value) % 2 == 0:
    left = int(str_value[:len(str_value)//2])
    right = int(str_value[len(str_value)//2:])
    return blink(blink_times+1, left) + blink(blink_times+1, right)
  else:
    return blink(blink_times+1, value*2024)

count = 0
for v in initial:
  count += blink(0,v)

print(f"Answer: {count}")