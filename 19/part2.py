# input_file = open("19/example.txt")
input_file = open("19/input.txt")
input_lines = input_file.readlines()
input_file.close()

patterns = input_lines[0].strip().split(', ')

print(patterns)

cache_patterns = {}

# Count the number of patterns
def count_patterns(where):
  # End of string, so we've found all the patterns
  if len(where) == 0:
    return 1
  
  count = 0
  # Optimization: cache the results of known strings
  if( where in cache_patterns ):
    return cache_patterns[where]
  
  for p in patterns:
    if where.startswith(p):
      count += count_patterns(where[len(p):])
  
  # Optimization: store in cache the current result
  cache_patterns[where] = count
  return count

total_count = 0
for line in input_lines[2:]:
  line = line.strip()
  
  this_count = count_patterns(line)
  print(f"{line}: {this_count}")
  total_count += this_count

print(f"Answer: {total_count}")

print(f"Cached: {len(cache_patterns)}")