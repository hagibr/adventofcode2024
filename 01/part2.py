# input_file = open("01/example.txt")
input_file = open("01/input.txt")
input_lines = input_file.readlines()
input_file.close()

# Need to keep only the list from 1st column
list1 = []
# Score map/dictionary for every value
score = {}

# Parsing is a bit different from part1
for line in input_lines:
  c1, c2 = [int(v) for v in line.split()]
  list1.append(c1)
  # Populating the score map using 2nd column as key and the number of ocurrences as value
  if score.get(c2,None) is None:
    score[c2] = 1
  else:
    score[c2] = score[c2] + 1

similarity_score = 0

# Accumulating the product of 1st column value and it's ocurrence
for c1 in list1:
  if score.get(c1,None) is not None:
    similarity_score += c1*score[c1]

print(f"Answer: {similarity_score}")