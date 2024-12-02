# input_file = open("02/example.txt")
input_file = open("02/input.txt")
input_lines = input_file.readlines()
input_file.close()

count_safe = 0
for line in input_lines:
  report = [int(v) for v in line.split()]
  is_safe = False
  # Increasing?
  if( report[1] - report[0] in range(1,4) ):
    is_safe = True
    # Check if it keep increasing
    for c in range(2,len(report)):
      if( report[c] - report[c-1] not in range(1,4) ):
        is_safe = False
        break
  # Decreasing?
  elif( report[0] - report[1] in range(1,4) ):
    is_safe = True
    # Check if it keep decreasing
    for c in range(2,len(report)):
      if( report[c-1] - report[c] not in range(1,4) ):
        is_safe = False
        break
  # Still safe, let's increase the counter
  if is_safe:
    count_safe += 1
  # Now let's try to remove one entry and recheck the safety
  else:
    for i in range(len(report)):
      report2 = report[:i] + report[i+1 :]
      is_safe = False
      # Increasing?
      if( report2[1] - report2[0] in range(1,4) ):
        is_safe = True
        # Check if it keep increasing
        for c in range(2,len(report2)):
          if( report2[c] - report2[c-1] not in range(1,4) ):
            is_safe = False
            break
      # Decreasing?
      elif( report2[0] - report2[1] in range(1,4) ):
        is_safe = True
        # Check if it keep decreasing
        for c in range(2,len(report2)):
          if( report2[c-1] - report2[c] not in range(1,4) ):
            is_safe = False
            break
      if is_safe:
        count_safe += 1
        break
print(f"Answer: {count_safe}")