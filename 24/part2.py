# input_file = open("24/example.txt")
# input_file = open("24/example2.txt") 
input_file = open("24/input.txt")
input_lines = input_file.readlines()
input_file.close()


values = dict()
operations = dict()

for line in input_lines:
  if ':' in line:
    name_val = line.strip().split(':')
    name, val = name_val[0], int(name_val[1])
    values[name] = val
  elif "->" in line:
    var_oper = line.strip().split()
    v1, v2, oper, out = var_oper[0], var_oper[2], var_oper[1], var_oper[4]
    v1, v2 = sorted((v1,v2))
    if (v1,v2) not in operations:
      operations[(v1,v2)] = []
    operations[(v1,v2)].append((oper,out))
    
# print(values)
# print(operations)

# As it was informed, the circuits make an adder, and we know that this adder adds 2 44-bit numbers,
# returning at most a 45 bit number

# For the first bit, it's a half-adder, so we have
# x_0 XOR y_0 -> z_0
# x_0 AND y_0 -> c_1 (c_1 is the carry for the second bit)

# And for the remaining bits (n = 1 ultil 44) it's a full-addr:
# x_n XOR y_n -> p_n (p_n is the partial sum)
# x_n AND y_n -> a_n
# p_n XOR c_n -> z_n (partial sum plus carry makes the current output)
# p_n AND c_n -> b_n
# a_n OR b_n -> c_{n+1} (carry of the full-adder is a combinatory)

# As for bit 45, it's just the same as c_44, because we don't have x_45 and y_45
# a_44 OR b_44 = c_44 = z_45

# We can search for all lines with x_n and y_n and check who should be p_n and a_n
# We can search for all lines with XOR and AND but not x_n and y_n and define all p_n and c_n
# We can check of ever p_n XOR c_n results into a x_n
# We can check for every candidate for a_n and b_n appears as operands of an OR and the result is a c_k

# A XOR B, when A and B are not x_n and y_n MUST result in a z_n
# A AND B, where A and B are the same A and B above CAN'T result in a z_n
