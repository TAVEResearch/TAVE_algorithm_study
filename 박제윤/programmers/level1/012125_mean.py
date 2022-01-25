# date: 2022.01.25
# author: jeiyoon
from typing import List

def solution(arr: List[int]) -> int:
  return sum(arr) / len(arr)

# return = 2.5
# arr = [1,2,3,4]	

# return = 5
arr = [5, 5]

print(solution(arr))
