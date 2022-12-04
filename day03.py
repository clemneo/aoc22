import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def letter_to_priority(letter):
  priority = ord(letter)
  if 97 <= priority <= 122:
    priority -= 96
  elif 65 <= priority <= 90:
    priority -= 38
  return priority

def find_common_numbers(list1, list2):
  common_numbers = []
  list1 = sorted(list1)
  list2 = sorted(list2)
  i, j = 0, 0
  while True:
    if i >= len(list1) or j >= len(list2):
      break
    if list1[i] == list2[j]:
      common_numbers.append(list1[i])
      i += 1
      j += 1
    elif list1[i] < list2[j]:
      i += 1
    elif list1[i] > list2[j]:
      j += 1
  return common_numbers

def solver(part):
  input_file = open_file('input/day03.txt')

  if part == 1:
    total_priority = 0
    for line in input_file:
      item_list = list(map(letter_to_priority, list(line)))
      compartment_1, compartment_2 = item_list[:len(item_list)//2], item_list[len(item_list)//2:]
      total_priority += find_common_numbers(compartment_1, compartment_2)[0]
    return total_priority
  if part == 2:
    total_priority = 0
    three_elfs = []
    for i in range(len(input_file)):
      item = list(map(letter_to_priority, list(input_file[i])))
      three_elfs.append(item)
      if (i+1)%3 == 0:
        compartment_1, compartment_2, compartment_3 = three_elfs[0], three_elfs[1], three_elfs[2]
        first_two_common_numbers = find_common_numbers(compartment_1, compartment_2)
        total_priority += find_common_numbers(first_two_common_numbers, compartment_3)[0]
        three_elfs = []

    return total_priority



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))