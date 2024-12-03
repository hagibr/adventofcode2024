# input_file = open("03/example2.txt")
input_file = open("03/input.txt")
input_lines = input_file.readlines()
input_file.close()

import re

# Tested on regex101.com with example string
mul_re = re.compile("mul[(]\d+,\d+[)]")

acc_mul = 0

# Parsing split lines don't work, because the "do()" and "don't()" switches must be kept between lines
big_line = ''
for line in input_lines:
  big_line += line

# First, split into block of strings separated by "do()"
for block_do in big_line.split("do()"):
  # print(block_do)
  # Now, each block can have 0 or more "don't()".
  block_do_donts = block_do.split("don't()")
  # print(block_do_donts)
  # We can safely ignore all that is after the "don't()"
  block_only_do = block_do_donts[0]
  for mul in mul_re.findall(block_only_do):
    # print(mul)
    # Now we parse to find the 2 operands
    m0, m1 = [int(v) for v in mul[4:-1].split(',')]
    # print(m0, m1)
    # Finally, accumulate the product
    acc_mul += m0 * m1

print(f"Answer: {acc_mul}")