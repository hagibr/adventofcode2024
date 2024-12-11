# input_file = open("09/example.txt")
input_file = open("09/input.txt")
input_lines = input_file.readlines()
input_file.close()


# Just one line this time
input_line = input_lines[0].replace('\r','').replace('\n','')

# Parsing the input differently
file_id = 0
last_file = file_id
input_data = []
for i in range(0,len(input_line)):
  block_size = int(input_line[i])
  if i % 2 == 0:
    input_data.append([file_id, block_size])
    last_file = file_id
    file_id += 1
    
  elif block_size > 0:
    input_data.append([-1, block_size])
  
# print(input_data)

while last_file >= 0:
  to_insert = None
  where_insert = 0
  # Going right to left
  for j in range(len(input_data)-1,0,-1):
    # Found last file
    if input_data[j][0] == last_file:
      len_file = input_data[j][1]
      moved = False
      # Going left to right
      for i in range(j):
        # Found empty block
        if input_data[i][0] == -1:
          len_empty = input_data[i][1]
          # Exact match for length
          if len_empty >= len_file:
            input_data[i] = input_data[j][:]
            input_data[j][0] = -1
            if( len_empty > len_file ):
              to_insert = [-1, len_empty-len_file]
              where_insert = i+1
            moved = True
          if moved:
            break
      if moved:
        break
  if to_insert is not None:
    new_input_data = input_data[:where_insert]
    new_input_data.append(to_insert)
    new_input_data += input_data[where_insert:]
    input_data = new_input_data
  last_file -= 1
    
# print(input_data)

checksum = 0
pos = 0
for entry in input_data:
  for len in range(entry[1]):
    if entry[0] != -1:
      checksum += entry[0]*pos
    pos += 1


print(f"Answer: {checksum}")