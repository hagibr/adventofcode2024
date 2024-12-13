# input_file = open("11/example.txt")
input_file = open("11/input.txt")
input_line = input_file.readline()
input_file.close()

initial = [int(v) for v in input_line.split()]

cache_results = {}

def blink(blink_times, value):
  if blink_times == 25:
    return 1
  
  if (blink_times, value) in cache_results:
    return cache_results[(blink_times, value)]
  
  str_value = str(value)
  if value == 0:
    result = blink(blink_times+1, 1)
    
  elif len(str_value) % 2 == 0:
    left = int(str_value[:len(str_value)//2])
    right = int(str_value[len(str_value)//2:])
    result = blink(blink_times+1, left) + blink(blink_times+1, right)
  else:
    result = blink(blink_times+1, value*2024)

  cache_results[(blink_times, value)] = result
  return result
  

count = 0
for v in initial:
  count += blink(0,v)

print(f"Answer: {count}")