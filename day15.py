import numpy as np
import pprint
pp = pprint.PrettyPrinter()


def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines


def manhattan_distance(p1, p2):
  return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


def point_occupied(info_dict, point, mh_dict):
  if point in info_dict.keys() or point in info_dict.values():
    return False

  for sensor, beacon in info_dict.items():
    point_dist = manhattan_distance(sensor, point)
    sensor_dist = mh_dict[(sensor)]
    if sensor_dist >= point_dist:
      return True
  return False


def generate_perimeter(sensor, coverage):
  x, y = sensor
  coverage += 1
  perimeter = []
  perimeter += [(x+i, y+coverage-i) for i in range(coverage)]
  perimeter += [(x+coverage-i, y-i) for i in range(coverage)]
  perimeter += [(x-i, y-coverage+i) for i in range(coverage)]
  perimeter += [(x-coverage+i, y+i) for i in range(coverage)]
  return perimeter


def solver(part):
  input_file = open_file('input/day15.txt')
  info_dict = {}
  global_y_locs = []
  global_x_locs = []
  for line in input_file:
    line_list = line.split()
    sx, sy = int(line_list[2][2:-1]), int(line_list[3][2:-1])
    bx, by = int(line_list[-2][2:-1]), int(line_list[-1][2:])
    info_dict[(sx,sy)] = (bx,by)
    global_y_locs += [sy, by]
    global_x_locs += [sx, bx]
  
  min_x, max_x = min(global_x_locs), max(global_x_locs)

  if part == 1:
    occupied_count = 0

    mh_dict = {}
    for sensor, beacon in info_dict.items():
      mh_dict[sensor] = manhattan_distance(sensor,beacon)
      
    for x in range(min_x-1000000, max_x+1000000):
      if point_occupied(info_dict, (x, 2000000), mh_dict):
        occupied_count += 1
    return occupied_count


  if part == 2:
    occupied_count = 0
    mh_dict = {}
    for sensor, beacon in info_dict.items():
      mh_dict[sensor] = manhattan_distance(sensor,beacon)
    
    perimeter_dict = {}
    for i, (sensor, coverage) in enumerate(mh_dict.items()):
      sensor_perimeters = generate_perimeter(sensor, coverage)
      for point in sensor_perimeters:
        if point not in perimeter_dict:
          perimeter_dict[point] = 1
        else:
          perimeter_dict[point] += 1

    good_points = [point for point, count in perimeter_dict.items() if count >= 4]
    for point in good_points:
      if not point_occupied(info_dict, point, mh_dict):
        return point[0] * 4000000 + point[1]



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))