input_file = open("21/example.txt") 
# input_file = open("21/input.txt")
input_lines = input_file.readlines()
input_file.close()

keys = [line.strip() for line in input_lines]

num_pad = [['7','8','9'],
           ['4','5','6'],
           ['1','2','3'],
           [' ','0','A']]
dir_pad = [[' ','^','A'],
           ['<','v','>']]

num_map = dict()
for r, line in enumerate(num_pad):
  for c, val in enumerate(line):
    num_map[val] = (r,c)
    num_map[(r,c)] = val

opt_num_map = dict()

dir_map = dict()
for r, line in enumerate(dir_pad):
  for c, val in enumerate(line):
    dir_map[val] = (r,c)
    dir_map[(r,c)] = val

print(num_map)
print(dir_map)

# Let's do a naive approach here
def get_num_sequence(text_in):
  # Initializing the robots at 'A'
  seq_pos = num_map['A']
  sequence = ''
  for c in text_in:
    # If the current character of the input is the not the same as the current sequence position
    while c != num_map[seq_pos]:
      c_pos = num_map[c]
      
      # If we must go right
      while( c_pos[1] > seq_pos[1] and num_map[(seq_pos[0], seq_pos[1]+1)] != ' '):
        sequence += '>'
        seq_pos = (seq_pos[0], seq_pos[1]+1)

      # If we must go up
      while( c_pos[0] < seq_pos[0] and num_map[(seq_pos[0]-1, seq_pos[1])] != ' '):
        sequence += '^'
        seq_pos = (seq_pos[0]-1, seq_pos[1])

      # If we must go down
      while( c_pos[0] > seq_pos[0] and num_map[(seq_pos[0]+1, seq_pos[1])] != ' '):
        sequence += 'v'
        seq_pos = (seq_pos[0]+1, seq_pos[1])

      # If we must go left
      while( c_pos[1] < seq_pos[1] and num_map[(seq_pos[0], seq_pos[1]-1)] != ' '):
        sequence += '<'
        seq_pos = (seq_pos[0], seq_pos[1]-1)

    sequence += 'A'
  return sequence

dir_to_dir = {
  ('^','^') : ['A'],
  ('^','A') : ['>A'],
  ('^','<') : ['v<A'],
  ('^','v') : ['vA'],
  ('^','>') : ['>vA'],

  ('A','^') : ['<A'],
  ('A','A') : ['A'],
  ('A','<') : ['v<<A'],
  ('A','v') : ['<vA'],
  ('A','>') : ['vA'],

  ('<','^') : ['>^A'],
  ('<','A') : ['>>^A'],
  ('<','<') : ['A'],
  ('<','v') : ['>A'],
  ('<','>') : ['>>A'],

  ('v','^') : ['^A'],
  ('v','A') : ['>^A'],
  ('v','<') : ['<A'],
  ('v','v') : ['A'],
  ('v','>') : ['>A'],

  ('>','^') : ['<^A'],
  ('>','A') : ['^A'],
  ('>','<') : ['<<A'],
  ('>','v') : ['<A'],
  ('>','>') : ['A'],
}

def get_dir_sequence(text_in):
  sequence = ''
  curr_c = 'A'
  for c in text_in:
    sequence += dir_to_dir[(curr_c,c)][0]
    curr_c = c
  return sequence

complexity = 0
for k in keys:
  robot1_sequence = get_num_sequence(k)
  robot2_sequence = get_dir_sequence(robot1_sequence)
  my_sequence = get_dir_sequence(robot2_sequence)
  print(my_sequence)
  print(robot2_sequence)
  print(robot1_sequence)
  print(k)
  my_len = len(my_sequence)
  k_val = int(k.replace('A',''))
  print(my_len, k_val)
  complexity += my_len*k_val

print(f"Answer: {complexity}")

# 165340: Too high