import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line)
  return output_lines

def read_instructions(line):
  left, destination = line.split(' to ')
  left, origin = left.split(' from ')
  left, amount = left.split(' ')

  return (int(amount), int(origin), int(destination.strip()))

def read_crates(line):
  crates = [line[i*4-3] for i in range(1,10)]
  return crates

def solver(part):
  input_file = open_file('input/day05.txt')

  # Reading crates
  crates = [[] for _ in range(9)]
  crate_lines = input_file[:8]
  for line in crate_lines:
    crate_line = read_crates(line)
    i = 0
    for crate in crate_line:
      if crate == ' ':
        i += 1
      else:
        crates[i].insert(0,crate)
        i += 1

  # Reading instructions
  instructions = input_file[10:]
  instructions = list(map(read_instructions, instructions))

  if part == 1:
    for amount, origin, destination in instructions:
      for _ in range(amount):
        crates[destination-1].append(crates[origin-1].pop())
        
    top_crates = [item[-1] for item in crates]
    return ''.join(top_crates)
    
  if part == 2:
    for amount, origin, destination in instructions:
      moved_crates = crates[origin-1][-amount:]
      crates[origin-1] = crates[origin-1][:-amount]
      crates[destination-1].extend(moved_crates)

    top_crates = [item[-1] for item in crates]
    return ''.join(top_crates)



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))