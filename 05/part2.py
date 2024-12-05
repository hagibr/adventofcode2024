# input_file = open("05/example.txt")
input_file = open("05/input.txt")
input_lines = input_file.readlines()
input_file.close()

# It's a map, with the left (the page that must be before) as key, and the list of pages that must be after
order_list = {}
update_list = []

# Parsing the lines from input file
for line in input_lines:
  # It's an ordering rule
  if '|' in line:
    before,after = [int (v) for v in line.split('|')]
    # Appending to list if not empty, and creating an unitary list when empty
    if( before in order_list ):
      order_list[before].append(after)
    else:
      order_list[before] = [after]
  # It's an update
  elif ',' in line:
    update_list.append([int (v) for v in line.split(',')])

# print(order_list)
# print(update_list)

sum_middle = 0

# Let's analyze the update list
for update in update_list:
  is_sorted = True
  
  for i in range(0,len(update)-1):
    before = update[i]
    if( before not in order_list ):
      is_sorted = False
      break
    for j in range(i+1,len(update)):
      if update[j] not in order_list[before]:
        is_sorted = False
        break
  
  # Now it's part 2
  if not is_sorted:
    # This is our comparison function
    def compare(a,b):
      if a in order_list and b in order_list[a]:
        return 1
      elif b in order_list and a in order_list[b]:
        return -1
      return 0  
    # We need to convert a comparison function into the lambda key function used by sorted()
    import functools

    # Sorting and then accumulate the middle page
    sorted_update = sorted(update, key=functools.cmp_to_key(compare))
    sum_middle += sorted_update[len(sorted_update)//2]

print(f"Answer: {sum_middle}")