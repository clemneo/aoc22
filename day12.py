import numpy as np
import networkx as nx
import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def check_connection(input_grid, point, direction):
  try:
    point_value = ord(input_grid[point])
    if direction == 'U':
      new_point = (point[0]-1, point[1])
    if direction == 'D':
      new_point = (point[0]+1, point[1])
    if direction == 'L':
      new_point = (point[0], point[1]-1)
    if direction == 'R':
      new_point = (point[0], point[1]+1)

    new_point_value = ord(input_grid[new_point])
    if new_point_value <= (point_value + 1):
      return new_point
    else:
      return None

  except IndexError:
    return None # 

def solver(part):
  input_file = open_file('input/day12.txt')
  input_file = [list(line) for line in input_file]

  input_grid = np.array(input_file)

  # Find the start and end
  start_search = np.where(input_grid == "S")
  starting = list(zip(start_search[0], start_search[1]))[0]
  end_search = np.where(input_grid == "E")
  ending = list(zip(end_search[0], end_search[1]))[0]
  
  # Replace them with their values
  input_grid[starting] = 'a'
  input_grid[ending] = 'z'

  # Setting up graph
  G = nx.DiGraph()
  for x in range(input_grid.shape[0]):
    for y in range(input_grid.shape[1]):
      for direction in ['U', 'D', 'L', 'R']:
        connected_node = check_connection(input_grid, (x,y), direction)

        if connected_node is not None:
          G.add_edge((x,y), connected_node)


  if part == 1:
    shortest_path = nx.shortest_path(G, starting, ending)

    return len(shortest_path)-1 # -1 to remove the start

  if part == 2:
    a_positions = np.where(input_grid == 'a')
    a_positions = list(zip(a_positions[0], a_positions[1]))
    steps_required = []
    for a_pos in a_positions:
      try:
        shortest_path = nx.shortest_path(G, a_pos, ending)
      except:
        continue
      steps_required.append(len(shortest_path)-1)

    return min(steps_required)



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))