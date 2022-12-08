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

def traverse_column(input_grid, grid_mask, column_no):
  relevant_column = input_grid[:, column_no]

  for i in range(1, len(relevant_column)):
    if relevant_column[i] > max(relevant_column[:i]):
      grid_mask[i, column_no] = 1

  for i in range(len(relevant_column)-2, 0, -1):
    if relevant_column[i] > max(relevant_column[i+1:]):
      grid_mask[i, column_no] = 1

def traverse_row(input_grid, grid_mask, row_no):
  relevant_row = input_grid[row_no, :]

  for i in range(1, len(relevant_row)):
    if relevant_row[i] > max(relevant_row[:i]):
      grid_mask[row_no, i] = 1

  for i in range(len(relevant_row)-2, 0, -1):
    if relevant_row[i] > max(relevant_row[i+1:]):
      grid_mask[row_no, i] = 1

def calc_scenic_score(input_grid, tree_location):
  tree_row, tree_col = tree_location
  tree_height = input_grid[tree_location]

  # Go left
  left = 0
  for i in range(tree_col-1,-1,-1):
    left += 1
    if input_grid[tree_row, i] >= tree_height:
      break

  # Go right
  right = 0
  for i in range(tree_col+1, input_grid.shape[1], 1):
    right += 1
    if input_grid[tree_row, i] >= tree_height:
      break

  # Go up
  up = 0
  for i in range(tree_row-1, -1, -1):
    up += 1
    if input_grid[i, tree_col] >= tree_height:
      break

  # Go down
  down = 0
  for i in range(tree_row+1, input_grid.shape[0], 1):
    down += 1
    if input_grid[i, tree_col] >= tree_height:
      break

  return left*right*up*down

def solver(part):
  input_file = open_file('input/day08.txt')
  input_grid = [list(map(int,line)) for line in input_file]
  input_grid = np.array(input_grid)

  if part == 1:
    grid_mask = np.zeros(input_grid.shape)
    grid_mask[0,:] = 1
    grid_mask[-1,:] = 1
    grid_mask[:,0] = 1
    grid_mask[:,-1] = 1
    num_rows, num_columns = input_grid.shape

    for row in range(num_rows):
      traverse_row(input_grid, grid_mask, row)

    for column in range(num_columns):
      traverse_column(input_grid, grid_mask, column)

    return np.sum(grid_mask)

  if part == 2:
    score_grid = np.zeros(input_grid.shape)
    for i in range(input_grid.shape[0]):
      for j in range(input_grid.shape[1]):
        score_grid[i,j] = calc_scenic_score(input_grid, (i,j))

    return np.max(score_grid)



print("Part 1: ", solver(1))
print("Part 2: ", solver(2))