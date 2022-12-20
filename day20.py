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

def solver(part):
  input_file = open_file('input/day20.txt')
  input_list = [int(line) for line in input_file]

  if part == 1:
    input_list_modified = [(index, number) for index, number in enumerate(input_list)]
    for id in range(len(input_list_modified)):
      print(id, end='\r')
      number = list(filter(lambda x: x[0] == id, input_list_modified))[0][1]
      current_index = input_list_modified.index((id, number))
      new_index = (current_index + number) % (len(input_list)-1)
      if new_index == 0:
        new_index = len(input_list)-1
      input_list_modified.pop(current_index)
      input_list_modified.insert(new_index, (id, number))
    input_list = [pair[1] for pair in input_list_modified]

    zero_index = input_list.index(0)
    grove_1 = (zero_index + 1000) % len(input_list)
    grove_2 = (zero_index + 2000) % len(input_list)
    grove_3 = (zero_index + 3000) % len(input_list)
    return input_list[grove_1] + input_list[grove_2] + input_list[grove_3]
  if part == 2:
    decryption_key = 811589153
    input_list_modified = [(index, number*decryption_key) for index, number in enumerate(input_list)]
    for i in range(10):
      print(f"Round {i}/10")
      for id in range(len(input_list_modified)):
        print(id, end='\r')
        number = list(filter(lambda x: x[0] == id, input_list_modified))[0][1]
        current_index = input_list_modified.index((id, number))
        new_index = (current_index + number) % (len(input_list)-1)
        if new_index == 0:
          new_index = len(input_list)-1
        input_list_modified.pop(current_index)
        input_list_modified.insert(new_index, (id, number))
    input_list = [pair[1] for pair in input_list_modified]


    zero_index = input_list.index(0)
    grove_1 = (zero_index + 1000) % len(input_list)
    grove_2 = (zero_index + 2000) % len(input_list)
    grove_3 = (zero_index + 3000) % len(input_list)
    return input_list[grove_1] + input_list[grove_2] + input_list[grove_3]
    return None



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))