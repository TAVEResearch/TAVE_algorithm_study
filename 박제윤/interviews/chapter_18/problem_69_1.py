# page: p537
# sol.1) from top right corner
# A[row][column]

# The best strategy is: (1) binary searching on the column first, (2) and then doing the same thing on the row -> However, It needs O(N)

# Simple strategy: Choose the last component on the first row,
# and then "target < component": "move left" & "target > component": "move down" 
from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
  # exception
  if not matrix:
    return False

  # the last component on the first row
  row = 0 
  col = len(matrix[0]) -1 # 4
  
  while row <= len(matrix) - 1 and col >= 0:
    if target == matrix[row][col]:
      return True
    elif target < matrix[row][col]:
      col -= 1
    elif target > matrix[row][col]:
      row += 1
    else:
      pass

  return False

matrix = [[1,4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]

# result = True
# target = 5 

#result = False 
target = 20

print(searchMatrix(matrix, target))
