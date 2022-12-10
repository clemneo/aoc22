import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

def update_head(head, direction):
  x_change = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
  y_change = {'U': 1, 'D': -1, 'L': 0, 'R': 0}

  return (head[0]+x_change[direction], head[1]+y_change[direction])

def update_tail(tail, new_head):
  x_pos_diff = tail[0] - new_head[0]
  y_pos_diff = tail[1] - new_head[1]

  if abs(x_pos_diff) >= 2 and abs(y_pos_diff) >= 2:
    tail = (tail[0] - x_pos_diff//2, tail[1] - y_pos_diff//2)
    return tail

  if abs(x_pos_diff) >= 2:
    tail = (tail[0] - x_pos_diff//2, new_head[1])
    return tail
  
  if abs(y_pos_diff) >= 2:
    tail = (new_head[0], tail[1] - y_pos_diff//2)
    return tail
  
  return tail

def solver(part):
  input_file = open_file('input/day09.txt')
  input_list = [(dir, int(num)) for dir, num in (line.split() for line in input_file)]

  if part == 1:
    visited = []
    head = (0,0)
    tail = (0,0)
    for direction, amount in input_list:
      for _ in range(amount):
        new_head = update_head(head, direction)
        new_tail = update_tail(tail, new_head)
        visited.append(new_tail)
        head = new_head
        tail = new_tail
    return len(set(visited))
  if part == 2:
    visited = []
    knots = [(0,0)] * 10
    for direction, amount in input_list:
      for _ in range(amount):
        for i in range(9):
          head = knots[i]
          tail = knots[i+1]
          if i == 0:
            head = update_head(head, direction)
          new_tail = update_tail(tail, head)
          knots[i] = head
          knots[i+1] = new_tail
        current_tail = knots[9] + ()
        visited.append(current_tail)

    return len(set(visited))



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))