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
  input_file = open_file('input/day04.txt')
  input_list = []
  for line in input_file:
    elf1, elf2 = line.split(",")
    elf1 = tuple(map(int,elf1.split("-")))
    elf2 = tuple(map(int,elf2.split("-")))
    input_list.append((elf1, elf2))

  if part == 1:
    fully_contained = 0
    for elf1, elf2 in input_list:
      if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
        fully_contained += 1

    return fully_contained
  if part == 2:
    overlapping_pairs = 0
    for elf1, elf2 in input_list:
      if elf1[0] <= elf2[0] <= elf1[1] or elf2[0] <= elf1[0] <= elf2[1]:
        overlapping_pairs += 1
    
    return overlapping_pairs



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))