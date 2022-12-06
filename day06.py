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
  input_file = open_file('input/day06.txt')
  input_line = input_file[0]
  if part == 1:
    for i in range(4, len(input_line)+1):
      characters = input_line[i-4:i]
      if len(set(characters)) == 4:
        return i
  if part == 2:
    for i in range(14, len(input_line)+1):
      characters = input_line[i-14:i]
      if len(set(characters)) == 14:
        return i



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))