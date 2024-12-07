# input_file = open("07/example.txt")
input_file = open("07/input.txt")
input_lines = input_file.readlines()
input_file.close()

# Main recursive function to execute the sum or multiplication OR CONCATENATION
def do_math(expected, operands):
  count_operands = len(operands)
  # Shouldn't happen, but let's be conservative
  if count_operands == 0:
    return False
  # Edge case when we start with only one operand
  elif count_operands == 1:
    return expected == operands[0]
  # 2 or more operands
  sum = operands[0] + operands[1]
  product = operands[0] * operands[1]
  concatenation = int(str(operands[0]) + str(operands[1]))
  # 2 operands: it's faster to check now instead of going a level down
  if count_operands == 2:
    return sum == expected or product == expected or concatenation == expected
  # Now we will test recursively the 3 operations
  sum_operands = [sum] + operands[2:]
  product_operands = [product] + operands[2:]
  concatenation_operands = [concatenation] + operands[2:]
  
  return do_math(expected, sum_operands) or do_math(expected, product_operands) or do_math(expected, concatenation_operands)

# Parsing the input and executing our calculations
total_calibration = 0
for line in input_lines:
  data_split = line.replace(':','').split()
  expected = int(data_split[0])
  operands = [int(v) for v in data_split[1:]]
  if do_math(expected, operands):
    total_calibration += expected

print(f"Answer: {total_calibration}")