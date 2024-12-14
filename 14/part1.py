# input_file = open("14/example.txt")
input_file = open("14/input.txt")
input_lines = input_file.readlines()
input_file.close()

# Example
# cols, rows, seconds = 11, 7, 100
# Input
cols, rows, seconds = 101, 103, 100

q1, q2, q3, q4 = 0, 0, 0, 0

for line in input_lines:
  p, v = line.split()
  px,py = [int(a) for a in p[2:].split(',')]
  vx,vy = [int(a) for a in v[2:].split(',')]
  # print(px,py,vx,vy)

  px = (px+vx*seconds) % cols
  py = (py+vy*seconds) % rows

  # 1st quadrant
  if px < (cols-1)//2 and py < (rows-1)//2:
    q1 += 1
  # 2nd quadrant
  elif px > (cols-1)//2 and py < (rows-1)//2:
    q2 += 1
  # 3rd quadrant
  elif px < (cols-1)//2 and py > (rows-1)//2:
    q3 += 1
  # 4th quadrant
  elif px > (cols-1)//2 and py > (rows-1)//2:
    q4 += 1

print(q1, q2, q3, q4)
print(f"Answer: {q1*q2*q3*q4}")