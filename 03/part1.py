# input_file = open("03/example.txt")
input_file = open("03/input.txt")
input_lines = input_file.readlines()
input_file.close()

import re

# Tested on regex101.com with example string
mul_re = re.compile("mul[(]\d+,\d+[)]")

acc_mul = 0
for line in input_lines:
  # print(line)
  # First we find all ocurrences of our pattern
  for mul in mul_re.findall(line):
    # print(mul)
    # Now we parse to find the 2 operands
    m0, m1 = [int(v) for v in mul[4:-1].split(',')]
    # print(m0, m1)
    # Finally, accumulate the product
    acc_mul += m0 * m1

print(f"Answer: {acc_mul}")