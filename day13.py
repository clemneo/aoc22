import ast
from functools import cmp_to_key
import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def evaluate_pair(item1, item2):
  if isinstance(item1, list) and isinstance(item2, list):
    left_is_smaller = len(item1) < len(item2)
    min_size = min(len(item1), len(item2))
    for i in range(min_size):
      element_1 = item1[i]
      element_2 = item2[i]
      test = evaluate_pair(element_1, element_2)
      if test is None:
        continue
      elif test:
        return True
      else:
        return False
    
    if len(item1) == len(item2):
      return None

    return left_is_smaller

  if isinstance(item1, int) and isinstance(item2, int):
    if item1 == item2:
      return None
    return item1 < item2

  left = [item1] if isinstance(item1, int) else item1
  right = [item2] if isinstance(item2, int) else item2

  return evaluate_pair(left, right)

def solver(part):
  input_file = open_file('input/day13.txt')
  input_lines = [ast.literal_eval(line) if line != "" else None for line in input_file]
  input_list = []
  input_item = []
  for line in input_lines:
    if line == None:
      input_list.append(input_item)
      input_item = []
      continue
    input_item.append(line)
  input_list.append(input_item)

  if part == 1:
    indices = []
    for index, pair in enumerate(input_list):
      if evaluate_pair(pair[0], pair[1]):
        indices.append(index+1)
    return sum(indices)

  if part == 2:
    full_input_list = []
    for pair in input_list:
      full_input_list += pair

    full_input_list += [[[2]], [[6]]]

    def evaluate_pair_adapter(item1, item2):
      result = evaluate_pair(item1, item2)
      if result == None: return 0
      if result == True: return 1
      if result == False: return -1

    sorted_list = sorted(full_input_list, key=cmp_to_key(evaluate_pair_adapter), reverse=True)

    return (sorted_list.index([[2]])+1)*(sorted_list.index([[6]])+1)


print("Part 1: ", solver(1))
print("Part 2: ", solver(2))