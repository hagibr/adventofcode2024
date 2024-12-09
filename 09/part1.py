# input_file = open("09/example.txt")
input_file = open("09/input.txt")
input_lines = input_file.readlines()
input_file.close()


# Just one line this time
input_line = input_lines[0].replace('\r','').replace('\n','')

# Parsing the input 
file_id = 0
input_data = [file_id]*int(input_line[0])
count_empty = 0
for i in range(1,len(input_line),2):
  file_id += 1
  empty_blocks = int(input_line[i])
  if empty_blocks:
    input_data += [-1]*empty_blocks
    count_empty += empty_blocks
  input_data += [file_id]*int(input_line[i+1])

# print(input_data, count_empty)

left = 0
right = len(input_data)-1

new_size = len(input_data) - count_empty

# Moving blocks
while( count_empty > 0 ):
  # Searching for the leftmost empty block
  while( input_data[left] != -1 ):
    left += 1
  # Searching for the rightmost non-empty block
  while( input_data[right] == -1 ):
    right -= 1
    count_empty -= 1
  # Moving the block from right to left
  input_data[left] = input_data[right]
  input_data[right] = -1
  count_empty -= 1
  # Updating the next indexes
  left += 1
  right -= 1
  # print(input_data, count_empty)

checksum = 0

for i in range(new_size):
  checksum += i * input_data[i]

print(f"Answer: {checksum}")