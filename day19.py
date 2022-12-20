from copy import deepcopy
import math
import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def can_buy_bot(blueprint, bot_count, resource_count):
  buyable_bots = {}
  print(blueprint)
  # bot_count = {'clay': 1, 'geode': 1, 'obsidian': 1, 'ore': 1}
  # resource_count = {'clay': 1, 'geode': 1, 'obsidian': 1, 'ore': 1}
  print(bot_count)
  print(resource_count)
  # exit()
  max_requirements = {
    'ore': max(blueprint['ore']['ore'], blueprint['clay']['ore'], blueprint['obsidian']['ore'], blueprint['geode']['ore']),
    'clay': blueprint['obsidian']['clay'],
    'obsidian': blueprint['geode']['obsidian'],
  }
  requirements_ordered = {
    'geode': blueprint['geode'],
    'obsidian': blueprint['obsidian'],
    'clay': blueprint['clay'],
    'ore': blueprint['ore']
  }
  for bot, requirements in requirements_ordered.items():
    # If bot isnt needed continue
    if bot != 'geode' and bot_count[bot] >= max_requirements[bot]:
      continue
    time = 0 # TODO: Might be bad
    for requirement in requirements:
      if bot_count[requirement] == 0:
        break
      else:
        time = max(time, math.ceil(blueprint[bot][requirement]-resource_count[requirement]//bot_count[requirement])) 
    else:
      buyable_bots[bot] = time

  print(buyable_bots)
  # exit()
  return buyable_bots

def buy_bot(blueprint, resource_count, bot_count, bot):
  if bot is None:
    return resource_count
  resource_needed = blueprint[bot]
  resource_count_new = deepcopy(resource_count)
  for resource, count_needed in resource_needed.items():
    resource_count_new[resource] -= count_needed
  bot_count[bot] += 1

  if resource_count_new[resource] < 0:
    print(bot_count)
    print(resource_count)
    print(resource_count_new)
    exit()
  return resource_count_new

def add_resources(bot_count, resource_count, time):
  for bot, count in bot_count.items():
    resource_count[bot] += count * time

  return resource_count

def run_simulation_naive(blueprint, bot_count, resource_count, time_left, time_jump, bot_to_buy):
  print("AAAAAAA")
  # print(time_left, time_jump)
  print(time_left, bot_count)
  # input()
  if time_left - time_jump < 0:
    resource_count = add_resources(bot_count, resource_count, time_left)
    return resource_count
  else:
    time_left -= time_jump
    resource_count = add_resources(bot_count, resource_count, time_jump)
    resource_count = buy_bot(blueprint, resource_count, bot_count, bot_to_buy)

  buyable_bots = can_buy_bot(blueprint, bot_count, resource_count)

  returns = [resource_count]
  for bot, time_needed in buyable_bots.items():
    # print(bot, time_needed)
    bot_count_new = deepcopy(bot_count)
    resource_count_new = deepcopy(resource_count)
    resource_count_new = run_simulation_naive(blueprint, bot_count_new, resource_count_new, time_left, time_needed, bot)
    returns.append(resource_count_new)

  return max(returns, key=lambda x:x['geode'])


def get_blueprint_output(blueprint):
  bot_count = {'clay': 0, 'geode': 0, 'obsidian': 0, 'ore': 1}
  resource_count = {'clay': 0, 'geode': 0, 'obsidian': 0, 'ore': 0}
  returns = run_simulation_naive(blueprint, bot_count, resource_count, 24, 0, None)
  print(returns)
  return returns

def solver(part):
  input_file = open_file('input/day19_test.txt')
  input_dict = {}
  for line in input_file:
    line = line.split()
    input_dict[int(line[1][:-1])] = {'ore': {line[7][:-1]: int(line[6])}, 'clay': {line[13][:-1]: int(line[12])},
                                  'obsidian': {line[19]: int(line[18]), line[22][:-1]:int(line[21])}, 'geode': {line[28]: int(line[27]), line[31][:-1]: int(line[30])}}
  # pp.pprint(input_dict)

  if part == 1:
    quality_level_total = 0
    for blueprint_no in input_dict:
      max_geodes = get_blueprint_output(input_dict[blueprint_no])
      quality_level_total += blueprint_no * max_geodes
    return quality_level_total
  if part == 2:
    return None



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))