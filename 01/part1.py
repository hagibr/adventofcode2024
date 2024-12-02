# input_file = open("01/example.txt")
input_file = open("01/input.txt")
input_lines = input_file.readlines()
input_file.close()

list1 = []
list2 = []

for line in input_lines:
  c1, c2 = [int(v) for v in line.split()]
  list1.append(c1)
  list2.append(c2)

list1.sort()
list2.sort()

total_distance = 0

for i in range(len(list1)):
  total_distance += abs(list1[i] - list2[i])

print(f"Answer: {total_distance}")