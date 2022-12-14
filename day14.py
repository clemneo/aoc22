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

def interpolate(p1, p2, include_end=False):
  points = []
  if p1[0] == p2[0]:
    for i in range(p1[1], p2[1], 1 if p1[1] <= p2[1] else -1):
      point = (p1[0], i)
      points.append(point)
  elif p1[1] == p2[1]:
    for i in range(p1[0], p2[0], 1 if p1[0] <= p2[0] else -1):
      point = (i, p1[1])
      points.append(point)
  if include_end:
    points.append(p2)
  return points

class Cave1:
  def __init__(self, rocks):
    self.rock_coordinates = []
    self.sand_coordinates = []
    self.last_sand_path = None
    for rock in rocks:
      # print(f"R: {rock}")
      for i in range(len(rock)-1):
        self.rock_coordinates += interpolate(rock[i], rock[i+1], include_end=(i == len(rock)-2))
    self.max_depth = max(self.rock_coordinates, key=lambda x: x[1])[1]
    # print(self.rock_coordinates)

  def add_sand(self, sand):
    if self.last_sand_path == None:
      current_path = [sand]
      stopped = False
      while not stopped:
        sand, stopped = self._move_sand(sand)
        current_path.append(sand)
      self.sand_coordinates.append(sand)
      self.last_sand_path = current_path
      return True

    if len(self.last_sand_path) == 2:
      return False

    current_path = self.last_sand_path[:-2]
    stopped = False
    sand = current_path[-1]
    while not stopped:
      sand, stopped = self._move_sand(sand)
      if sand[1] > self.max_depth:
        return False
      current_path.append(sand)
      self.sand_coordinates.append(sand)
    self.last_sand_path = current_path
    return True
    

  def _move_sand(self, sand):
    if (sand[0], sand[1]+1) not in self.rock_coordinates and (sand[0], sand[1]+1) not in self.sand_coordinates:
      return (sand[0], sand[1]+1), False
    elif (sand[0]-1, sand[1]+1) not in self.rock_coordinates and (sand[0]-1, sand[1]+1) not in self.sand_coordinates:
      return (sand[0]-1, sand[1]+1), False
    elif (sand[0]+1, sand[1]+1) not in self.rock_coordinates and (sand[0]+1, sand[1]+1) not in self.sand_coordinates:
      return (sand[0]+1, sand[1]+1), False
    else:
      return sand, True
    
class Cave2:
  def __init__(self, rocks):
    self.rock_coordinates = []
    self.sand_coordinates = []
    self.last_sand_path = None
    for rock in rocks:
      for i in range(len(rock)-1):
        self.rock_coordinates += interpolate(rock[i], rock[i+1], include_end=(i == len(rock)-2))
    self.max_depth = max(self.rock_coordinates, key=lambda x: x[1])[1]+2
    min_left = min(self.rock_coordinates, key=lambda x: x[0])[0]
    min_right = max(self.rock_coordinates, key=lambda x: x[0])[0]
    self.rock_coordinates += interpolate((min_left-1000, self.max_depth),(min_right+1000, self.max_depth))

  def add_sand(self, sand):
    if self.last_sand_path == None:
      current_path = [sand]
      stopped = False
      while not stopped:
        sand, stopped = self._move_sand(sand)
        current_path.append(sand)
      self.sand_coordinates.append(sand)
      self.last_sand_path = current_path
      return True

    if len(self.last_sand_path) == 2:
      return False

    current_path = self.last_sand_path[:-2]
    stopped = False
    sand = current_path[-1]
    while not stopped:
      sand, stopped = self._move_sand(sand)
      current_path.append(sand)
      self.sand_coordinates.append(sand)
    self.last_sand_path = current_path
    return True

  def _move_sand(self, sand):
    if (sand[0], sand[1]+1) not in self.rock_coordinates and (sand[0], sand[1]+1) not in self.sand_coordinates:
      return (sand[0], sand[1]+1), False
    elif (sand[0]-1, sand[1]+1) not in self.rock_coordinates and (sand[0]-1, sand[1]+1) not in self.sand_coordinates:
      return (sand[0]-1, sand[1]+1), False
    elif (sand[0]+1, sand[1]+1) not in self.rock_coordinates and (sand[0]+1, sand[1]+1) not in self.sand_coordinates:
      return (sand[0]+1, sand[1]+1), False
    else:
      return sand, True


def solver(part):
  input_file = open_file('input/day14.txt')
  rocks = []
  for line in input_file:
    rock_points = line.split(' -> ')
    rock_points = [tuple([int(rp) for rp in rock.split(',')]) for rock in rock_points]
    rocks.append(rock_points)


  if part == 1:
    cave = Cave1(rocks)
    sand_units= 0
    while cave.add_sand((500,0)):
      sand_units += 1
      print(sand_units, end='\r')
    return sand_units
  if part == 2:
    cave = Cave2(rocks)
    sand_units= 0
    while cave.add_sand((500,0)):
      sand_units += 1
      print(sand_units, end='\r')
    return sand_units



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))