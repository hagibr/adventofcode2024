# input_file = open("12/example.txt")
input_file = open("12/input.txt")
input_lines = input_file.readlines()
input_file.close()

area_rows = len(input_lines)
area_cols = len(input_lines[0]) - 1

# Mapping every coordinate to a region
region_map = {}
# List of all regions
region_list = []

# Search for same adjacent plants to include into the region
def search_region(region, r, c):
  # If the up coordinate is valid, the plant at this position is not into a region yet and it's the same type...
  if r > 0 and (r-1,c) not in region_map and input_lines[r-1][c] == input_lines[r][c]:
    region.append((r-1,c))
    region_map[(r-1,c)] = region
    search_region(region, r-1, c)
  if r < area_rows-1 and (r+1,c) not in region_map and input_lines[r+1][c] == input_lines[r][c]:
    region.append((r+1,c))
    region_map[(r+1,c)] = region
    search_region(region, r+1, c)
  if c > 0 and (r,c-1) not in region_map and input_lines[r][c-1] == input_lines[r][c]:
    region.append((r,c-1))
    region_map[(r,c-1)] = region
    search_region(region, r, c-1)
  if c < area_cols-1 and (r,c+1) not in region_map and input_lines[r][c+1] == input_lines[r][c]:
    region.append((r,c+1))
    region_map[(r,c+1)] = region
    search_region(region, r, c+1)

# This is the starting of region creation
for r in range(area_rows):
  for c in range(area_cols):
    # If this coordinate is not into a region yet...
    if (r,c) not in region_map:
      # It's because we need to create a new region
      new_region = [(r,c)]
      region_map[(r,c)] = new_region
      region_list.append(new_region)
      # Now search for adjacent plants
      search_region(new_region, r, c)

# Now we need to calculate the number of sides
def sides(region):
  return 1 # TODO

price = 0
for region in region_list:
  # first = region[0]
  # print(f"{input_lines[first[0]][first[1]]}: {region} {len(region)} {perimeter(region)}")
  price += len(region) * sides(region)
    
print(f"Answer: {price}")