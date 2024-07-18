def print_grid(grid):
  for row in grid:
      print(" ".join(str(num) if num != 0 else "." for num in row))

def find_empty_location(grid):
  for i in range(len(grid)):
      for j in range(len(grid[i])):
          if grid[i][j] == 0:
              return (i, j)
  return None

def is_safe(grid, row, col, num):
  # Check row
  if num in grid[row]:
      return False

  # Check column
  for i in range(len(grid)):
      if grid[i][col] == num:
          return False

  # Check 3x3 subgrid
  subgrid_row_start = (row // 3) * 3
  subgrid_col_start = (col // 3) * 3
  for i in range(3):
      for j in range(3):
          if grid[subgrid_row_start + i][subgrid_col_start + j] == num:
              return False

  return True

def solve_sudoku(grid):
  empty_location = find_empty_location(grid)
  if not empty_location:
      return True  # No more empty locations, puzzle solved
  row, col = empty_location

  for num in range(1, 10):
      if is_safe(grid, row, col, num):
          grid[row][col] = num

          if solve_sudoku(grid):
              return True

          grid[row][col] = 0  # Undo the move (backtracking)

  return False

# Example Sudoku grid (0 represents empty cells)
sudoku_grid = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Sudoku grid:")
print_grid(sudoku_grid)

if solve_sudoku(sudoku_grid):
  print("\nSolved Sudoku grid:")
  print_grid(sudoku_grid)
else:
  print("\nNo solution exists for the given Sudoku grid.")
