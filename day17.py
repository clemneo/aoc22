import numpy as np
import pprint
pp = pprint.PrettyPrinter()

def open_file(file):
  with open(file, 'r+') as f:
    lines = f.readlines()
  output_lines = []
  for line in lines:
    output_lines.append(line.strip())
  return output_lines

class Tile:
  def __init__(self, bottom_left_pos, shape_index):
    self.pos = bottom_left_pos
    self.shape = shape_index

  def __repr__(self):
    return str(self.pos)

  def move_left(self):
    already_left = (self.pos[0] == 0)
    if already_left:
      return self.output_self_points() # If already at the left edge return

    self.pos = (self.pos[0] - 1, self.pos[1])
    return self.output_self_points()

  def move_right(self):
    already_right = (self.shape == 0 and self.pos[0] == 3) \
                    or (self.shape == 1 and self.pos[0] == 4) \
                    or (self.shape == 2 and self.pos[0] == 4) \
                    or (self.shape == 3 and self.pos[0] == 6) \
                    or (self.shape == 4 and self.pos[0] == 5)
    if already_right:
      return self.output_self_points()
    else:
      self.pos = (self.pos[0] + 1, self.pos[1])
      return self.output_self_points()

  def move_down(self):
    self.pos = (self.pos[0], self.pos[1]-1)
    return self.output_self_points()

  def move_up(self):
    self.pos = (self.pos[0], self.pos[1]+1)
    return self.output_self_points()

  def output_self_points(self):
    x, y = self.pos
    if self.shape == 0: # -
      return [(x,y), (x+1, y), (x+2, y), (x+3, y)]
    if self.shape == 1: # +
      return [(x+1, y), (x, y+1), (x+1,y+1), (x+1, y+2), (x+2, y+1)]
    if self.shape == 2: # reverse L
      return [(x,y), (x+1, y), (x+2, y), (x+2, y+1), (x+2, y+2)]
    if self.shape == 3: # |
      return [(x,y), (x, y+1), (x, y+2), (x, y+3)]
    if self.shape == 4: # square
      return [(x,y), (x+1, y), (x, y+1), (x+1, y+1)]
    


def solver(part):
  input_file = open_file('input/day17.txt')
  # input_file = ['>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>']
  input_list = list(input_file[0])
  print(len(input_list))

  rocks = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0)]

  if part == 1:
    tick = 0
    rocks_dropped = 0
    top_level = 0
    current_rock = Tile((2,4), rocks_dropped % 5)
    rock_has_dropped = False
    while True:
      input_char = input_list[tick % len(input_list)] # Get wind direction
      tick += 1
      if rock_has_dropped: # Spawn new rock if needed
        rocks_dropped += 1
        if rocks_dropped == 2022:
          break
        rock_has_dropped = False
        current_rock = Tile((2, top_level + 4), rocks_dropped % 5)

      # Run wind to the left/right
      if input_char == '<':
        rock_points = current_rock.move_left()
        for point in rock_points:
          if point in rocks:
            current_rock.move_right()
            break
      elif input_char == '>':
        rock_points = current_rock.move_right()
        for point in rock_points:
          if point in rocks:
            current_rock.move_left()
            break
      # Run drop
      rock_points = current_rock.move_down()
      for point in rock_points:
        if point in rocks:
          rock_points = current_rock.move_up()
          rock_has_dropped = True
          # print(rock_points)
          rocks += rock_points
          # print(rocks)
          top_level = max(top_level, sorted(rock_points, key = lambda x: x[1], reverse=True)[0][1])
          # 
          # grid = np.full((100,7), '.', dtype=str)
          # np.put(grid, rocks, '#')
          # for rock_x, rock_y in rocks:
            # grid[rock_y, rock_x] = '#'
          # for rock_x, rock_y in rock_points:
            # grid[rock_y, rock_x] = '#'
          # grid = np.flipud(grid)
          # for line in grid:
            # print(''.join(list(line)))
          print(rocks_dropped, top_level)
          # input()
          # input()
          break


    return top_level

  if part == 2:
    top_levels = []
    tick = 0
    rocks_dropped = 0
    top_level = 0
    current_rock = Tile((2,4), rocks_dropped % 5)
    rock_has_dropped = False
    while True:
      input_char = input_list[tick % len(input_list)] # Get wind direction
      tick += 1
      if rock_has_dropped: # Spawn new rock if needed
        rocks_dropped += 1
        if rocks_dropped == 20220:
          break
        rock_has_dropped = False
        current_rock = Tile((2, top_level + 4), rocks_dropped % 5)

      # Run wind to the left/right
      if input_char == '<':
        rock_points = current_rock.move_left()
        for point in rock_points:
          if point in rocks:
            current_rock.move_right()
            break
      elif input_char == '>':
        rock_points = current_rock.move_right()
        for point in rock_points:
          if point in rocks:
            current_rock.move_left()
            break
      # Run drop
      rock_points = current_rock.move_down()
      for point in rock_points:
        if point in rocks:
          rock_points = current_rock.move_up()
          rock_has_dropped = True
          # print(rock_points)
          rocks += rock_points
          top_level = max(top_level, sorted(rock_points, key = lambda x: x[1], reverse=True)[0][1])
          top_levels.append(top_level)
          break
    new_top_levels = [top_levels[0]]
    for i in range(len(top_levels)-1):
      new_top_levels.append(top_levels[i+1]-top_levels[i])


    # Find substrings
    from collections import Counter
    a=''.join(list(map(str,new_top_levels)))
    print(a)
    times=5
    for n in range(1,len(a)//times+1)[::-1]:
        substrings=[a[i:i+n] for i in range(len(a)-n+1)]
        freqs=Counter(substrings)
        if freqs.most_common(1)[0][1]>=3:
            seq=freqs.most_common(1)[0][0]
            break
    print("sequence '%s' of length %s occurs %s or more times"%(seq,n,times))

def guess_seq_len(seq):
    guess = 1
    max_len = len(seq) // 2
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
            return x

    return guess
    



# print("Part 1: ", solver(1))
# print("Part 2: ", solver(2))

# A bit lazy to build a pattern matcher, so I manually inspected the print output and did this
first_window = '13320021300330013340132010122001222133001234013302133201232013240130321232000120132201230002222133221330013240022221320013242123001300202340133421330012220122201130212220103001302002300132221320212122133000232013320132221222213302003201031213002122001303010310030201332012302023001322013302132121332013210'
repeated_window = '1334002300132201303203001132021320013322122001330002120121221222012120113021321103220113401334000320130221230002220133221330212301132221320003220130021230213320133400030013042133221332013220133400330013212023221230013200132201332013200133021330002040022120121003342123001322212302123010320013202123021330013030013001232013342122401332012120132400013200320132101212013300133000122013300123221302012301121221330213322121421332002140022221320013320132201324000340020001330013222133000220203032001221330012140133021330012210033201230103322122221321203320121300121012220133000230013042132201022013020123000304013211130321300113300132201230213010133201300213320122201334013322123401334012220023201320013020132400020013220123401334013300132201304213030020400322010340133201321113200133401330013302133021330212220132201302013200022001324012120123001332212220123401302212222133001230202142132001213012322132001330013220132001232012300132100320113030032200221201210130321330012300133001330213300132001322013342033201303012302121301222013302132111031013302123001321113322133021230212300133201230013300133201332213000122401334013222130300330013020133400200013340003000330012122123021332012120123400224012110123201330013300023021330013240133021302013002132221303000101133201304013342033220232213212013021222013320133000032013300122201320012122022220013002240023401222200320132001030012100132201324013030032001320012222132221300212301133000230011220023001230013042132400030212202132021232012220132221322212132023201330013222133021330212322133421234012130033201321003300132200222213302003401031213220133001324000120123001324000300133001320212200121400034212200130400320013300130401032013300013021320013300133201334013302'
new_top_levels = list(map(int,list(first_window + repeated_window)))
total_needed = 1000000000000
top_level = 0
top_level = sum(new_top_levels[:len(first_window)]) # added 15 here
top_level_repeated = new_top_levels[len(first_window):len(first_window)+len(repeated_window)]
total = top_level + (total_needed-len(first_window))//len(top_level_repeated) * sum(top_level_repeated) + sum(top_level_repeated[:(total_needed-len(first_window))%len(top_level_repeated)])
print(total)