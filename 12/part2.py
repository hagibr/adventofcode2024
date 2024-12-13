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
  UP = 1
  DOWN = 2
  LEFT = 4
  RIGHT = 8
  # Mapping every coordinate to a set of borders
  border_map = {}
  # At first, every coordinate have all borders
  for r in region:
    border_map[r] = UP | DOWN | LEFT | RIGHT

  # Now we have to eliminate the borders of adjacent coordinates
  for i in range(len(region)-1):
    ri, ci = region[i]
    for j in range(i+1,len(region)):
      rj, cj = region[j]
      # Same row
      if ri == rj:
        # One column difference, region i at right of region j
        if ci - cj == 1:
          # Remove the border at right of region i
          border_map[region[i]] &= ~RIGHT
          # Remove the border at left of region j
          border_map[region[j]] &= ~LEFT
        # One column difference, region j at right of region i
        elif cj - ci == 1:
          # Remove the border at left of region i
          border_map[region[i]] &= ~LEFT
          # Remove the border at right of region j
          border_map[region[j]] &= ~RIGHT
          
      # Same column
      elif ci == cj:
        # One row difference, region j below region i
        if rj - ri == 1:
          # Remove the border at bottom of region i
          border_map[region[i]] &= ~DOWN
          # Remove the border at top of region j
          border_map[region[j]] &= ~UP
        # One row difference, region i below region j
        elif ri - rj == 1:
          # Remove the border at top of region i
          border_map[region[i]] &= ~UP
          # Remove the border at bottom of region j
          border_map[region[j]] &= ~DOWN
  
  count_sides = 0
  # Finally, we need the borders into sides
  for block in region:
    # Get the remaining borders
    bi = border_map[block]
    # We need at least 1 border
    if bi == 0:
      continue

    ri, ci = block
    # UP border
    if bi & UP:
      # Creating a new side
      count_sides += 1
      # And we can remove this border from this block
      border_map[block] &= ~UP
      
      # Checking going left
      r, c = ri, ci-1
      # While we are still finding blocks at left and these blocks have the UP border...
      while (r,c) in region and border_map[(r,c)] & UP:
        # We group this border into our current side
        border_map[(r,c)] &= ~UP
        # Next block at left...
        c = c-1
      # Checking going right
      r, c = ri, ci+1
      while (r,c) in region and border_map[(r,c)] & UP:
        border_map[(r,c)] &= ~UP
        c = c+1
    # DOWN border
    if bi & DOWN:
      # Creating a new side
      count_sides += 1
      # And we can remove this border from this block
      border_map[block] &= ~DOWN
      
      # Checking going left
      r, c = ri, ci-1
      while (r,c) in region and border_map[(r,c)] & DOWN:
        border_map[(r,c)] &= ~DOWN
        c = c-1
      # Checking going right
      r, c = ri, ci+1
      while (r,c) in region and border_map[(r,c)] & DOWN:
        border_map[(r,c)] &= ~DOWN
        c = c+1
    # LEFT border
    if bi & LEFT:
      # Creating a new side
      count_sides += 1
      # And we can remove this border from this block
      border_map[block] &= ~LEFT
      
      # Checking going up
      r, c = ri-1, ci
      while (r,c) in region and border_map[(r,c)] & LEFT:
        border_map[(r,c)] &= ~LEFT
        r=r-1
      # Checking going down
      r, c = ri+1, ci
      while (r,c) in region and border_map[(r,c)] & LEFT:
        border_map[(r,c)] &= ~LEFT
        r=r+1
    # RIGHT border
    if bi & RIGHT:
      # Creating a new side
      count_sides += 1
      # And we can remove this border from this block
      border_map[block] &= ~RIGHT
      
      # Checking going up
      r, c = ri-1, ci
      while (r,c) in region and border_map[(r,c)] & RIGHT:
        border_map[(r,c)] &= ~RIGHT
        r=r-1
      # Checking going down
      r, c = ri+1, ci
      while (r,c) in region and border_map[(r,c)] & RIGHT:
        border_map[(r,c)] &= ~RIGHT
        r=r+1
  return count_sides


price = 0
for region in region_list:
  first = region[0]
  print(f"{input_lines[first[0]][first[1]]}: {region} {len(region)} {sides(region)}")
  price += len(region) * sides(region)
    
print(f"Answer: {price}")