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
  
  if is_sorted:
    # accumulate the middle page
    sum_middle += update[len(update)//2]

print(f"Answer: {sum_middle}")