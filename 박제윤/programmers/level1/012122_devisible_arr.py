# date: 2022.01.21
# author: jeiyoon
from typing import List

def solution(arr: List[int], divisor: int) -> List[int]:
  result = []
  for a in sorted(arr):
    if not a % divisor:
      result.append(a)
  if len(result) == 0:
    return [-1]
  else:
    return result

# return = [5, 10]
# arr = [5, 9, 7, 10]
# divisor = 5 

# return = [1, 2, 3, 36]
# arr = [2, 36, 1, 3]
# divisor = 1


# return = 	[-1]
arr = [3,2,6]
divisor = 10

print(solution(arr, divisor))
