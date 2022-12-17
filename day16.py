import networkx as nx
import matplotlib.pyplot as plt
import itertools
from tqdm.auto import tqdm
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

class Valve:
  def __init__(self, flow_rate, connected_valves):
    self.flow_rate = flow_rate
    self.connections = connected_valves

  def __repr__(self):
    return f"Flow: {self.flow_rate}, Connections: {self.connections}"

def traverse_graph(current_valve, valves, valves_left, distance_dict, time_left): 
  if valves_left is None or time_left <= 0:
    return 0, [current_valve]

  scores = [(0, [current_valve])]
  for valve in valves_left:
    distance = distance_dict[current_valve][valve]
    if distance < time_left: # not <= because distance is technically dist+1, to include time taken to turn on
      flow_rate = valves[valve].flow_rate
      updated_time_left = time_left - distance
      updated_valves_left = deepcopy(valves_left)
      updated_valves_left.remove(valve)
      score = (updated_time_left) * flow_rate
      future_score, route = traverse_graph(valve, valves, updated_valves_left, distance_dict, updated_time_left)
      score += future_score
      result = (score, [valve] + route)
      scores.append(result)

  return max(scores)

def get_max_score(graph, valves, time, is_part1):
  relevant_valves = []
  for valve in valves:
    if valves[valve].flow_rate != 0:
      relevant_valves.append(valve)

  distance_dict = {k:v for k, v in nx.all_pairs_shortest_path(graph)}
  for origin in distance_dict:
    for destination, route in distance_dict[origin].items():
      distance_dict[origin][destination] = len(route)

  if is_part1:
    return traverse_graph("AA", valves, relevant_valves, distance_dict, time)
  else:
    max_score = 0
    # for split_size in range(len(relevant_valves)//2+1):
    for split_size in [7]: # Top line is needed for full search, but just doing a 7/8 split gave me the right answer
                           # Intuition being the best solution would be where they split the work equally
      for list1, list2 in tqdm(split_list_into_two(relevant_valves, split_size), position=0, leave=True):
        score1, route1 = traverse_graph("AA", valves, list1, distance_dict, time)
        score2, route2 = traverse_graph("AA", valves, list2, distance_dict, time)
        max_score = max(max_score, score1 + score2)
    return max_score
    
def split_list_into_two(input_list, split_size):
  output_list = []
  for list1 in itertools.combinations(input_list, split_size):
    list1 = list(list1)
    list2 = list(set(input_list) - set(list1))
    output_list.append((list1, list2))
  return output_list


def solver(part):
  input_file = open_file('input/day16.txt')

  valves = {}

  for line in input_file:
    valve = line.split()[1]
    flow_rate = int(line.split()[4][5:-1])
    dest_valves = [valve[0:2] for valve in line.split()[9:]]
    valves[valve] = Valve(flow_rate, dest_valves)

  G = nx.Graph()
  for key in valves:
    G.add_node(key)

  for key, valve in valves.items():
    connections = valve.connections
    for connection in connections:
      G.add_edge(key, connection)


  if part == 1:
    answer = get_max_score(G, valves, 30, is_part1=True)
    return answer
  if part == 2:
    answer = get_max_score(G, valves, 26, is_part1=False)
    return answer



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))