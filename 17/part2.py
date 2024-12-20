# input_file = open("17/example2.txt")
input_file = open("17/input.txt")
input_lines = input_file.readlines()
input_file.close()

# Just parsing
A = B = C = 0
Program = []
for line in input_lines:
  if line.startswith("Register A: "):
    corrupted_A = int(line[12:])
  elif line.startswith("Register B: "):
    initial_B = int(line[12:])
  elif line.startswith("Register C: "):
    initial_C = int(line[12:])
  elif line.startswith("Program: "):
    Program = [int(p) for p in line[9:].split(',')]

# print(A,B,C,Program)

# Analysis:
# My input program is 2,4,1,1,7,5,4,7,1,4,0,3,5,5,3,0
# Let's decompile it (8 instructions):
# 1st: 2,4 -> bst cmb_A [B = A % 8]
# 2nd: 1,1 -> bxl lit_1 [B = B ^ 1]
# 3rd: 7,5 -> cdv cmb_A [C = A // 2**B]
# 4th: 4,7 -> bxc       [B = B ^ C]
# 5th: 1,4 -> bxl lit_4 [B = B ^ 4]
# 6th: 0,3 -> adv cmb_3 [A = A // 2**3]
# 7th: 5,5 -> out B     [outputs current value at B modulo 8]
# 8th: 3,0 -> jnz 0     [if A not 0, jump to 1st instruction]

# Let's translate them into Python code
def run_program(value_A):
  # Initialization
  A = value_A
  B = C = 0
  out = []
  # Loop
  while (A != 0):     # jnz 0
    B = A % 8         # bst cmb_A
    B = B ^ 1         # bxl lit_1
    C = A >> B        # cdv cmb_A
    B = B ^ C         # bxc
    B = B ^ 4         # bxl lit_4
    A = A // 8        # adv cmb_3
    out.append(B % 8) # out B
    # This is an optimization for our implementation: exiting when we know that we already know that A is not right
    if( out != Program[:len(out)]) : break
  return out
  
# I've tried to make sense by reversing the operations, without success. So I've changed my approach.

# Iterative solution. As we saw that we shift A by 3 bits on every loop, and we want 16 outputted values,
# Then the lowest candidate is 8**(16-1) and it should be lower than 8**16

# For our iteration, let's implement a helper function
def iterator(offset, increment):
  value_A = 8**15 + offset # This is the initial value. Minimum of 8**15 to have 16 outputted values
  count = 0
  while(value_A < 8**16): # Maximum of 8**16, because it would give us 17 outputted values
    out = run_program(value_A)
    # Debugging the evolution of the number of outputted values
    if( len(out) > count or out == Program[:len(out)]):
      count = len(out)
      # Printing the decimal value, binary value, outputted value and number of elements of output
      print(value_A, bin(value_A), out, count)
      if( out == Program ):
        break
    value_A += increment
  return value_A # Only when we found the value

# This is the first loop that I've tried. Incrementing one by one.
# answer = iterator(0,1)

# This loop gave me these 5 outputs at the first 30 seconds
# 35184372088832 0b1000000000000000000000000000000000000000000000 [5] 1
# 35184372088839 0b1000000000000000000000000000000000000000000111 [2, 5] 2
# 35184372089043 0b1000000000000000000000000000000000000011010011 [2, 4, 6] 3
# 35184372089386 0b1000000000000000000000000000000000001000101010 [2, 4, 1, 5] 4
# 35184372099626 0b1000000000000000000000000000000010101000101010 [2, 4, 1, 1, 7, 5, 5] 7

# Now it's time to do some inference here. It seems that the last 6 bits must be be 0b101010
# So now we increment by 0b1000000
# answer = iterator( 0b101010,
#                   0b1000000)

# OK, some progress. Now the output is:
# 35184372088874 0b1000000000000000000000000000000000000000101010 [2, 0] 2
# 35184372089386 0b1000000000000000000000000000000000001000101010 [2, 4, 1, 5] 4
# 35184372099626 0b1000000000000000000000000000000010101000101010 [2, 4, 1, 1, 7, 5, 5] 7
# 35184378915370 0b1000000000000000000000011010000010101000101010 [2, 4, 1, 1, 7, 5, 4, 6] 8
# 35184618514986 0b1000000000000000001110101100000010101000101010 [2, 4, 1, 1, 7, 5, 4, 7, 3] 9

# Now the last bits are 0b10101000101010, so we increment by 0b100000000000000
# answer = iterator( 0b10101000101010,
#                   0b100000000000000)

# 35184372099626 0b1000000000000000000000000000000010101000101010 [2, 4, 1, 1, 7, 5, 5] 7
# 35184378915370 0b1000000000000000000000011010000010101000101010 [2, 4, 1, 1, 7, 5, 4, 6] 8
# 35184618514986 0b1000000000000000001110101100000010101000101010 [2, 4, 1, 1, 7, 5, 4, 7, 3] 9
# 35187857041962 0b1000000000000011001111101110000010101000101010 [2, 4, 1, 1, 7, 5, 4, 7, 1, 5] 10
# 35190255659562 0b1000000000000101011110101100000010101000101010 [2, 4, 1, 1, 7, 5, 4, 7, 1, 4, 0, 5] 1

# There are some problems here, so let's be conservative and keep just the last bits and change the increment
# answer = iterator(      0b10101000101010,
#                   0b10000000000000000000)

# 35184372099626 0b1000000000000000000000000000000010101000101010 [2, 4, 1, 1, 7, 5, 5] 7
# 35184378915370 0b1000000000000000000000011010000010101000101010 [2, 4, 1, 1, 7, 5, 4, 6] 8
# 35184618514986 0b1000000000000000001110101100000010101000101010 [2, 4, 1, 1, 7, 5, 4, 7, 3] 9
# 35187857041962 0b1000000000000011001111101110000010101000101010 [2, 4, 1, 1, 7, 5, 4, 7, 1, 5] 10
# 35190255659562 0b1000000000000101011110101100000010101000101010 [2, 4, 1, 1, 7, 5, 4, 7, 1, 4, 0, 5] 12
# 35241258396202 0b1000000000110100111110101100000010101000101010 [2, 4, 1, 1, 7, 5, 4, 7, 1, 4, 0, 3, 5, 5, 1] 15

# ALmost there, it seems that the iteration with output size 10 was the wrong one. Let's use the matching
# parts of size 12 and size 15
answer = iterator( 0b11110101100000010101000101010,
                  0b100000000000000000000000000000)


print(f"Answer: {answer}")