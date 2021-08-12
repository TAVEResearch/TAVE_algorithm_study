# page: p538
# sol.2) any() <-> all(): p540
# https://blockdmask.tistory.com/430
from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
  print([row for row in matrix])
  return any(target in row for row in matrix)

matrix = [[1,4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]

# result = True
target = 5 

#result = False 
# target = 20

print(searchMatrix(matrix, target))
