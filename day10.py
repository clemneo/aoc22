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
  input_file = open_file('input/day10.txt')

  x = 1
  cycle_values = {}
  cycle = 1
  for line in input_file:
    if line == 'noop':
      cycle_values[cycle] = x
      cycle += 1
    else:
      amount = int(line.split()[1])
      cycle_values[cycle] = x
      cycle_values[cycle+1] = x
      x += amount
      cycle += 2
  
  if part == 1:
    cycles_needed = [20,60,100,140,180,220]
    sum = 0
    for cycle in cycles_needed:
      sum += cycle * cycle_values[cycle]
    return sum
  if part == 2:
    picture = ([],[],[],[],[],[])
    for row in range(6):
      for col in range(1,41):
        cycle_num = row*40+col # +1 because of zero indexing
        x = cycle_values[cycle_num]
        sprite_pixels = [x, x+1, x+2]
        if col in sprite_pixels:
          picture[row].append('#')
        else:
          picture[row].append('.')

    picture = [''.join(pixels) for pixels in picture]
    pp.pprint(picture)
    return None



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))