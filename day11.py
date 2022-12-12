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
  input_file = open_file('input/day11.txt')

  input_dict = {
    0: {
      'start': [71, 86],
      'op': lambda old: old * 13,
      'test': lambda num: True if num%19 == 0 else False,
      True: 6,
      False: 7,
      'inspect_count': 0
    },
    1: {
      'start': [66, 50, 90, 53, 88, 85],
      'op': lambda old: old + 3,
      'test': lambda num: True if num%2 == 0 else False,
      True: 5,
      False: 4,
      'inspect_count': 0
    },
    2: {
      'start': [97, 54, 89, 62, 84, 80, 63],
      'op': lambda old: old + 6,
      'test': lambda num: True if num%13 == 0 else False,
      True: 4,
      False: 1,
      'inspect_count': 0
    },
    3: {
      'start': [82, 97, 56, 92],
      'op': lambda old: old + 2,
      'test': lambda num: True if num%5 == 0 else False,
      True: 6,
      False: 0,
      'inspect_count': 0
    },
    4: {
      'start': [50, 99, 67, 61, 86],
      'op': lambda old: old * old,
      'test': lambda num: True if num%7 == 0 else False,
      True: 5,
      False: 3,
      'inspect_count': 0
    },
    5: {
      'start': [61, 66, 72, 55, 64, 53, 72, 63],
      'op': lambda old: old + 4,
      'test': lambda num: True if num%11 == 0 else False,
      True: 3,
      False: 0,
      'inspect_count': 0
    },
    6: {
      'start': [59, 79, 63],
      'op': lambda old: old * 7,
      'test': lambda num: True if num%17 == 0 else False,
      True: 2,
      False: 7,
      'inspect_count': 0
    },
    7: {
      'start': [55],
      'op': lambda old: old + 7,
      'test': lambda num: True if num%3 == 0 else False,
      True: 2,
      False: 1,
      'inspect_count': 0
    },
  }

  if part == 1:
    for _ in range(20):
      for monkey_no in input_dict:
        monkey = input_dict[monkey_no]
        for item in monkey['start']:
          item = monkey['op'](item)
          item = item//3
          is_divisible = monkey['test'](item)
          new_monkey = monkey[is_divisible]
          input_dict[new_monkey]['start'].append(item)
          monkey['inspect_count'] += 1
        monkey['start'] = []
    
    monkey_businesses = []
    for monkey_no in input_dict:
      monkey = input_dict[monkey_no]
      monkey_businesses.append(monkey['inspect_count'])

    monkey_businesses = sorted(monkey_businesses, reverse=True)

    return monkey_businesses[0]*monkey_businesses[1]
    
  if part == 2:
    for i in range(10000):
      for monkey_no in input_dict:
        monkey = input_dict[monkey_no]
        for item in monkey['start']:
          item = monkey['op'](item)
          item = item % 9699690 # Multiple of all the tests' prime numbers
          is_divisible = monkey['test'](item)
          new_monkey = monkey[is_divisible]
          input_dict[new_monkey]['start'].append(item)
          monkey['inspect_count'] += 1
        monkey['start'] = []
    
    monkey_businesses = []
    for monkey_no in input_dict:
      monkey = input_dict[monkey_no]
      monkey_businesses.append(monkey['inspect_count'])

    monkey_businesses = sorted(monkey_businesses, reverse=True)

    return monkey_businesses[0]*monkey_businesses[1]



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))