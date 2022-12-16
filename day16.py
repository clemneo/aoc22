import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def solver(part):
  input_file = open_file('input/day16.txt')

  if part == 1:
    return None
  if part == 2:
    return None



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))