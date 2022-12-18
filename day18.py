import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines
  

def check_adjacent(cubes, cube):
  x, y, z = cube
  adjacents = 0
  if (x+1, y, z) not in cubes: adjacents += 1
  if (x-1, y, z) not in cubes: adjacents += 1
  if (x, y+1, z) not in cubes: adjacents += 1
  if (x, y-1, z) not in cubes: adjacents += 1
  if (x, y, z+1) not in cubes: adjacents += 1
  if (x, y, z-1) not in cubes: adjacents += 1

  return adjacents


def check_adjacent_inside(cubes, cube):
  x, y, z = cube
  adjacents = 0
  if (x+1, y, z) in cubes: adjacents += 1
  if (x-1, y, z) in cubes: adjacents += 1
  if (x, y+1, z) in cubes: adjacents += 1
  if (x, y-1, z) in cubes: adjacents += 1
  if (x, y, z+1) in cubes: adjacents += 1
  if (x, y, z-1) in cubes: adjacents += 1

  return adjacents


def get_inside_area(cubes, pockets):
  total_inside_area = 0
  for pocket in pockets:
    total_inside_area += check_adjacent_inside(cubes, pocket)
  return total_inside_area


def get_pockets(cubes):
  min_x = min(cubes, key=lambda x: x[0])[0]
  max_x = max(cubes, key=lambda x: x[0])[0]
  min_y = min(cubes, key=lambda x: x[1])[1]
  max_y = max(cubes, key=lambda x: x[1])[1]
  min_z = min(cubes, key=lambda x: x[2])[2]
  max_z = max(cubes, key=lambda x: x[2])[2]
  outside_pockets = []
  pending_pockets = [(0,0,0)]
  while len(pending_pockets) != 0:
    # print(pending_pockets)
    pocket = pending_pockets.pop()
    outside_pockets.append(pocket)
    x, y, z = pocket
    if x-1 >= min_x and (x-1, y, z) not in cubes and (x-1, y, z) not in outside_pockets:
        pending_pockets.append((x-1, y, z))
    if x+1 <= max_x and (x+1, y, z) not in cubes and (x+1, y, z) not in outside_pockets:
        pending_pockets.append((x+1, y, z))
    if y-1 >= min_y and (x, y-1, z) not in cubes and (x, y-1, z) not in outside_pockets:
        pending_pockets.append((x, y-1, z))
    if y+1 <= max_y and (x, y+1, z) not in cubes and (x, y+1, z) not in outside_pockets:
        pending_pockets.append((x, y+1, z))
    if z-1 >= min_z and (x, y, z-1) not in cubes and (x, y, z-1) not in outside_pockets:
        pending_pockets.append((x, y, z-1))
    if z+1 <= max_z and (x, y, z+1) not in cubes and (x, y, z+1) not in outside_pockets:
        pending_pockets.append((x, y, z+1))
  
  inside_pockets = []
  for x in range(min_x, max_x):
    for y in range(min_y, max_y):
      for z in range(min_z, max_z):
        if (x,y,z) not in outside_pockets and (x,y,z) not in cubes:
          inside_pockets.append((x,y,z))

  return inside_pockets


def solver(part):
  input_file = open_file('input/day18.txt')
  input_list = [tuple(map(int,line.split(','))) for line in input_file]

  if part == 1:
    surface_area = 0
    for cube in input_list:
      surface_area += check_adjacent(input_list, cube)
    return surface_area
  if part == 2:
    surface_area = 0
    for cube in input_list:
      surface_area += check_adjacent(input_list, cube)
    pockets = get_pockets(input_list)
    surface_area -= get_inside_area(input_list, pockets)
    return surface_area



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))