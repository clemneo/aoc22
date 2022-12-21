from copy import deepcopy
import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def parse_dict_step(input_dict, is_part1):
  is_done = True
  for monkey, info in input_dict.items():
    if isinstance(info, int) or isinstance(info, float):
      continue

    op1, op2, operator = info
    if isinstance(input_dict[op1], tuple) or isinstance(input_dict[op2], tuple):
      is_done = False
      continue

    if not is_part1 and monkey == 'root':
      continue

    if operator == '+':
      input_dict[monkey] = input_dict[op1] + input_dict[op2]
    if operator == '-':
      input_dict[monkey] = input_dict[op1] - input_dict[op2]
    if operator == '*':
      input_dict[monkey] = input_dict[op1] * input_dict[op2]
    if operator == '/':
      input_dict[monkey] = input_dict[op1] / input_dict[op2]

  return is_done

def parse_dict(input_dict, is_part1):
  is_done = False
  while not is_done:
    is_done = parse_dict_step(input_dict, is_part1)

def solver(part):
  input_file = open_file('input/day21.txt')
  input_dict = {}
  for line in input_file:
    line = line.split()
    if len(line) == 2:
      name, number = line[0][:-1], int(line[1])
      input_dict[name] = number
    elif len(line) == 4:
      name, op1, operator, op2 = line
      name = name[:-1]
      input_dict[name] = (op1, op2, operator)


  if part == 1:

    parse_dict(input_dict, is_part1 = True)

    return int(input_dict['root'])

  if part == 2:

    input_dict_original = deepcopy(input_dict)
    you = 0
    step_size = 100_000_000_000
    learning_rate = 2
    delta = 1
    positive_or_negative = lambda x: 1 if x>0 else -1

    # While the two numbers are not equal
    while input_dict[input_dict['root'][0]] != input_dict[input_dict['root'][1]]:
      you += int(step_size * learning_rate) * positive_or_negative(delta)
      input_dict = deepcopy(input_dict_original)
      input_dict['humn'] = you
      parse_dict(input_dict, is_part1 = False)
      delta = input_dict[input_dict['root'][0]] - input_dict[input_dict['root'][1]]
      learning_rate *= 0.99
      if delta == 0: 
        break

    return you



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))