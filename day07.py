import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

class Node:
  def __init__(self, type, name, size, parent):
    self.name = name
    self.type = type
    self.size = size
    self.parent = parent
    self.children = []

  def add_child(self, child):
    self.children.append(child)

  def find_child(self, child_name):
    for child in self.children:
      if child.name == child_name:
        return child
    return None

def update_dir_size(node):
  dir_size = 0
  for child in node.children:
    if child.type == 'file':
      dir_size += child.size
    elif child.type == 'dir':
      dir_size += update_dir_size(child)
  node.size = dir_size
  return dir_size

def get_dir_sizes(node, list):
  for child in node.children:
    if child.type == 'dir':
      get_dir_sizes(child, list)
  list.append((node.size, node.name))

def solver(part):
  input_file = open_file('input/day07.txt')

  # Parse input
  base_node = Node('dir', '/', 0, None)
  current_node = base_node
  i = 0
  while i < len(input_file):
    line = input_file[i]
    if line[:5] == '$ cd ': # If cding into directory
      dir = line [5:]
      if dir == '..':
        current_node = current_node.parent
      else:
        child = current_node.find_child(dir)
        if child == None:
          child = Node('dir', dir, 0, current_node)
          current_node.add_child(child)
        current_node = child
    elif line == '$ ls':
      line = input_file[i+1]
      while line[0] != '$':
        left, right = line.split()
        if left == 'dir':
          child = Node('dir', right, 0, current_node)
          current_node.add_child(child)
        else:
          filesize = int(left)
          child = Node('file', right, filesize, current_node)
          current_node.add_child(child)
        i += 1
        if i+1 == len(input_file): 
          break
        line = input_file[i+1]

    i += 1
  
  update_dir_size(base_node)
  dir_sizes =[]
  get_dir_sizes(base_node, dir_sizes)

  if part == 1:
    answer = 0
    for dir_size, dir_name in dir_sizes:
      if dir_size <= 100000:
        answer += dir_size
    return answer
  if part == 2:
    total_size = 70000000
    unused_space = total_size - base_node.size
    space_needed = 30000000 - unused_space

    for dir_size, dir_name in sorted((dir_sizes)):
      if dir_size >= space_needed:
        return dir_size



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))