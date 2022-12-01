import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def total_elfs_calories(input):
    elf_totals = []
    current_elf = 0
    for line in input:
        if line == '':
            elf_totals.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    elf_totals.append(current_elf)
    return elf_totals

def solver(part):
  input_file = open_file('input/day01.txt')

  if part == 1:
    elf_totals = total_elfs_calories(input_file)
    return max(elf_totals)

  if part == 2:
    elf_totals = total_elfs_calories(input_file)
    return sum(sorted(elf_totals)[-3:])


print("Part 1: ", solver(1))
print("Part 2: ", solver(2))