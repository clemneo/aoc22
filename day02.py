import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def rps_score(opp, player, part):
  """ABC is Rock Paper Scissors, XYZ is Rock Paper Scissorz"""
  if part == 2:
    opp_player_adapter = {
      ('A', 'X'): 'Z',
      ('A', 'Y'): 'X',
      ('A', 'Z'): 'Y',

      ('B', 'X'): 'X',
      ('B', 'Y'): 'Y',
      ('B', 'Z'): 'Z',

      ('C', 'X'): 'Y',
      ('C', 'Y'): 'Z',
      ('C', 'Z'): 'X'
    }
    player = opp_player_adapter[(opp,player)]

  rps_outcome_score = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0, 

    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,

    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3
  }
  rps_choice_score = {
    'X': 1, 'Y': 2, 'Z': 3
  }

  return rps_outcome_score[(opp, player)] + rps_choice_score[player]


def solver(part):
  input_file = open_file('input/day02.txt')

  if part == 1:
    # pp.pprint(input_file)
    total_score = 0
    for line in input_file:
      opp, player = line.split(" ")
      total_score += rps_score(opp, player, part)
    return total_score
  if part == 2:
    total_score = 0
    for line in input_file:
      opp, player = line.split(" ")
      total_score += rps_score(opp, player, part)
    return total_score



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))